from django.db import models






class Doctor(models.Model):
    first_name = models.CharField(max_length=50, help_text="Imię lekarza.")
    last_name = models.CharField(max_length=50, help_text="Nazwisko lekarza.")
    specialty = models.CharField(max_length=100, help_text="Specjalizacja lekarza.")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.specialty}"
    

class MedicalProcedures(models.Model):
    procedure_name = models.CharField(max_length=100, help_text="Nazwa procedury medycznej.")
    description = models.TextField(help_text="Opis procedury medycznej.")
    cost = models.DecimalField(max_digits=10, decimal_places=2, help_text="Koszt procedury medycznej.")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, help_text="Lekarz wykonujący procedurę.")
    date = models.DateField(help_text="Data wykonania procedury.")
    date = models.DateTimeField(help_text="Data i czas wykonania procedury.")

    def __str__(self):
        return self.procedure_name

