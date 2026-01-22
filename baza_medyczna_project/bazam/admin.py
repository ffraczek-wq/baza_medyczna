from django.contrib import admin
from .models import Lekarz, Zabiegi, Osoba, Pacjent

class OsobaAdmin(admin.ModelAdmin):
    list_display = ["imie" , "nazwisko" , "stanowisko"]
    list_filter = ["stanowisko" , "data_dodania"]

admin.site.register(Osoba, OsobaAdmin)



admin.site.register(Lekarz)
admin.site.register(Zabiegi)
admin.site.register(Pacjent)


