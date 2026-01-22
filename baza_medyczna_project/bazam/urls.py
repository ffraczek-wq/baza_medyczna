from django.urls import path
from . import views

urlpatterns = [
    path('lekarze/', views.doctor_list, name='doctor_list'),
]