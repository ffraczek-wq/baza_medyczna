from django.shortcuts import render
from .models import Lekarz

def lista_doktorow(request):
    from .models import Lekarz
    lekarze = Lekarz.objects.all()
    return render(request, 'bazam/lista_doktorow.html', {'lekarze': lekarze})
