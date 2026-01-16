from django.contrib import admin

class OsobaAdmin(admin.ModelAdmin):
    list_display = ["imie" , "nazwisko" , "stanowisko"]
    list_filter = ["stanowisko" , "data_dodania"]

admin.site.register(Osoba, OsobaAdmin)

from .models import Doctor, MedicalProcedures, Osoba

admin.site.register(Doctor)
admin.site.register(MedicalProcedures)


