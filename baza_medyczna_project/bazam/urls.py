from django.urls import path
from . import views

urlpatterns = [
    path('lekarze/', views.lista_doktorow, name='lista_doktorow'),

    path('', views.strona_glowna, name='strona_glowna'),
]
