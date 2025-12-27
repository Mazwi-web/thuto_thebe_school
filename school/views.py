from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import render
from .models import Announcement

from .models import Application
from django.shortcuts import render, redirect

def home(request):
    latest_announcements = Announcement.objects.order_by('-date_posted')[:3]
    return render(request, 'school/home.html', {
        'latest_announcements': latest_announcements
    })


def about(request):
    return render(request, 'school/about.html')


def academics(request):
    return render(request, 'school/academics.html')


def staff(request):
    return render(request, 'school/staff.html')


def announcements(request):
    announcements = Announcement.objects.order_by('-date_posted')
    return render(request, 'school/announcements.html', {
        'announcements': announcements
    })


def sports(request):
    return render(request, 'school/sports.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject='New Contact Message - Thuto Thebe Secondary School',
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['mbulimazwi6@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'school/contact.html', {'success': True})

    return render(request, 'school/contact.html')

def application_form(request):
    if request.method == 'POST':
        Application.objects.create(
            learner_name=request.POST['learner_name'],
            learner_surname=request.POST['learner_surname'],
            age=request.POST['age'],
            id_number=request.POST['id_number'],
            parent_name=request.POST['parent_name'],
            parent_email=request.POST['parent_email'],
            parent_contact=request.POST['parent_contact'],
            learner_contact=request.POST['learner_contact'],
            home_address=request.POST['home_address'],
            province=request.POST['province'],
            previous_school=request.POST['previous_school'],
            career=request.POST['career'],
            motivation=request.POST['motivation'],
            learner_signature=request.POST['learner_signature'],
            parent_signature=request.POST['parent_signature'],
        )
        return redirect('application_success')

    return render(request, 'school/application.html')


def application_success(request):
    return render(request, 'school/application_success.html')