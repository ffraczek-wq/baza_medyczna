from django.urls import path
from . import views

urlpatterns = [
    path('', views.strona_glowna, name='strona_glowna'),
    path('lekarze/', views.lista_doktorow, name='lista_doktorow'),
    path('stanowiska/', views.stanowisko_lista, name='stanowisko-lista'),
    path('stanowiska/<int:id>/', views.stanowisko_detal, name='stanowisko-detal'),
]