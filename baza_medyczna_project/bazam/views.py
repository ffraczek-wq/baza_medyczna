from django.shortcuts import render

def lista_doktorow(request):
<<<<<<< HEAD
    doctors = Doctor.objects.all()
    return render(request, 'bazam/lista_doktorow.html', {'doctors': doctors})
=======
    from .models import Lekarz
    lekarze = Lekarz.objects.all()
    return render(request, 'bazam/lista_doktorow.html', {'lekarze': lekarze})
>>>>>>> dd35c92cf55a5238c56010203219ba43ec8effb8
