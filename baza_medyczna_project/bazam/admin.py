from django.contrib import admin

from .models import Doctor, MedicalProcedures

admin.site.register(Doctor)
admin.site.register(MedicalProcedures)
