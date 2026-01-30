from django.urls import path
from . import views

urlpatterns = [
    path('', views.strona_glowna, name='strona_glowna'),

    path('lekarze/', views.lista_doktorow, name='lista_doktorow'),

    path('zabiegi/', views.lista_zabiegow, name='lista_zabiegow'),

    path('koszyk/dodaj/<int:id>/', views.dodaj_do_koszyka, name='dodaj-do-koszyka'),
    
    path('koszyk/', views.pokaz_koszyk, name='pokaz-koszyk'),
]