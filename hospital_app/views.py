from django.shortcuts import render
from .models import Appointment

def home(request):
    return render(request, 'hospital_app/home.html')

def advanced_bed_facilities(request):
    return render(request, 'hospital_app/advanced_bed_facilities.html')

def dental_care(request):
    return render(request, 'hospital_app/dental_care.html')

def massage_therapy(request):
    return render(request, 'hospital_app/massage_therapy.html')

def cardiology(request):
    return render(request, 'hospital_app/cardiology.html')

def diagnosis(request):
    return render(request, 'hospital_app/diagnosis.html')

def ambulance_service(request):
    return render(request, 'hospital_app/ambulance_service.html')

def physiotherapy(request):
    return render(request, 'hospital_app/physiotherapy.html')

def free_checkup(request):
    return render(request, 'hospital_app/free_checkup.html')

def experts_consultancy(request):
    return render(request, 'hospital_app/experts_consultancy.html')

def pharmacy_medicine(request):
    return render(request, 'hospital_app/pharmacy_medicine.html')

def comprehensive_care(request):
    return render(request, 'hospital_app/comprehensive_care.html')

def book_appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        appointment_date = request.POST.get('appointment_date')

        # Save the data to the database
        Appointment.objects.create(
            name=name,
            phone_number=phone_number,
            email=email,
            appointment_date=appointment_date,
        )
        return redirect('home')  # Redirect to the homepage after submission
    return render(request, 'hospital_app/home.html')