from django.contrib import admin
from django.urls import path
from hospital_app.views import home, book_appointment
from hospital_app.views import (
    home,
    advanced_bed_facilities,
    dental_care,
    massage_therapy,
    cardiology,
    diagnosis,
    ambulance_service,
    physiotherapy,
    free_checkup,
    experts_consultancy,
    pharmacy_medicine,
    comprehensive_care,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('home/advanced_bed_facilities/', advanced_bed_facilities, name='advanced_bed_facilities'),
    path('home/dental_care/', dental_care, name='dental_care'),
    path('home/massage_therapy/', massage_therapy, name='massage_therapy'),
    path('home/cardiology/', cardiology, name='cardiology'),
    path('home/diagnosis/', diagnosis, name='diagnosis'),
    path('home/ambulance_service/', ambulance_service, name='ambulance_service'),
    path('home/physiotherapy/', physiotherapy, name='physiotherapy'),
    path('home/free_checkup/', free_checkup, name='free_checkup'),
    path('home/experts_consultancy/', experts_consultancy, name='experts_consultancy'),
    path('home/pharmacy_medicine/', pharmacy_medicine, name='pharmacy_medicine'),
    path('home/comprehensive_care/', comprehensive_care, name='comprehensive_care'),
    path('home/book-appointment/', book_appointment, name='book_appointment'),
]