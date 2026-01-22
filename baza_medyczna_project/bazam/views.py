from django.shortcuts import render
from .models import Doctor

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'bazam/doctor_list.html', {'doctors': doctors})