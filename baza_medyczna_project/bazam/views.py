from django.shortcuts import render

def lista_doktorow(request):
    doctors = Doctor.objects.all()
    return render(request, 'bazam/lista_doktorow.html', {'doctors': doctors})
