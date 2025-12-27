from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.mail import send_mail
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


# =========================
# ANNOUNCEMENTS
# =========================
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# =========================
# CONTACT MESSAGES
# =========================
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


# =========================
# APPLICATIONS
# =========================
class Application(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    learner_name = models.CharField(max_length=100)
    learner_surname = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)

    id_number = models.CharField(max_length=13)

    parent_name = models.CharField(max_length=150)
    parent_email = models.EmailField()
    parent_contact = models.CharField(max_length=20)

    learner_contact = models.CharField(max_length=20)
    home_address = models.TextField(blank=True,null=True)

    address = models.TextField(blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)

    previous_school = models.CharField(max_length=150, blank=True, null=True)
    career = models.CharField(max_length=150, blank=True, null=True)

    motivation = models.TextField(blank=True, null=True)

    # FILE UPLOADS
    id_document = models.FileField(
        upload_to='applications/id_documents/',
        validators=[FileExtensionValidator(['pdf', 'jpg', 'jpeg', 'png'])],
        blank=True,
        null=True
    )

    learner_signature = models.ImageField(
        upload_to='applications/signatures/',
        blank=True,
        null=True
    )

    parent_signature = models.ImageField(
        upload_to='applications/signatures/',
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.learner_name} {self.learner_surname}"


# =========================
# EMAIL CONFIRMATION SIGNAL
# =========================
@receiver(post_save, sender=Application)
def send_application_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject="Application Received – Thuto Thebe Secondary School",
            message=(
                f"Dear {instance.parent_name},\n\n"
                f"The application for {instance.learner_name} {instance.learner_surname} "
                f"has been successfully received.\n\n"
                "We will communicate the outcome in due course.\n\n"
                "Regards,\n"
                "Thuto Thebe Secondary School"
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.parent_email],
            fail_silently=True,
        )
