from django.shortcuts import render, redirect, get_object_or_404
from .models import Zabiegi

def lista_doktorow(request):
    from .models import Lekarz
    lekarze = Lekarz.objects.all()
    return render(request, 'bazam/lista_doktorow.html', {'lekarze': lekarze})

def strona_glowna(request):
    return render(request, 'bazam/strona_glowna.html')

def lista_zabiegow(request):
    zabiegi = Zabiegi.objects.all()
    return render(request, 'bazam/lista_zabiegow.html', {'zabiegi': zabiegi})




def dodaj_do_koszyka(request, id):
    koszyk = request.session.get('koszyk', [])
    koszyk.append(id)
    request.session['koszyk'] = koszyk
    return redirect('lista_zabiegow')

def pokaz_koszyk(request):
    ids_w_koszyku = request.session.get('koszyk', [])
    wybrane_zabiegi = Zabiegi.objects.filter(id__in=ids_w_koszyku)
    suma = sum(zabieg.koszt for zabieg in wybrane_zabiegi)
    return render(request, 'bazam/koszyk.html', {
    'zabiegi': wybrane_zabiegi, 
    'suma': suma
    })