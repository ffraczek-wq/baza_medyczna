from django.shortcuts import render, get_object_or_404
from .models import Lekarz, Osoba, Stanowisko 

def lista_doktorow(request):
    lekarze = Lekarz.objects.all()
    return render(request, 'bazam/lista_doktorow.html', {'lekarze': lekarze})

def strona_glowna(request):
    return render(request, 'bazam/strona_glowna.html')

def stanowisko_lista(request):
    stanowiska = Stanowisko.objects.all()
    return render(request, 'bazam/stanowisko-lista.html', {'stanowiska': stanowiska})

def stanowisko_detal(request, id):
    stanowisko = get_object_or_404(Stanowisko, pk=id)
    return render(request, 'bazam/stanowisko-detal.html', {'stanowisko': stanowisko})