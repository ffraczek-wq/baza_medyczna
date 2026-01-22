from django.contrib import admin
from .models import Doctor, MedicalProcedures, Osoba, Pacjent

class OsobaAdmin(admin.ModelAdmin):
    list_display = ["imie" , "nazwisko" , "stanowisko"]
    list_filter = ["stanowisko" , "data_dodania"]

admin.site.register(Osoba, OsobaAdmin)



admin.site.register(Doctor)
admin.site.register(MedicalProcedures)
admin.site.register(Pacjent)


