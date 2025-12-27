from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('academics/', views.academics, name='academics'),
    path('staff/', views.staff, name='staff'),
    path('announcements/', views.announcements, name='announcements'),
    path('sports/', views.sports, name='sports'),  # ✅ THIS LINE MUST EXIST
    path('contact/', views.contact, name='contact'),
    
    path('apply/', views.application_form, name='application'),
path('apply/success/', views.application_success, name='application_success'),
]
