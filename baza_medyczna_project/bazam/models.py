from django.db import models


Dates = models.IntegerChoices(
     'Daty_Styczeń',
     '1.01 2.01 3.01 4.01 5.01 6.01 7.01 8.01 9.01 10.01 11.01 12.01 13.01 14.01 15.01 16.01 17.01 18.01 19.01 20.01 21.01 22.01 23.01 24.01 25.01 26.01 27.01 28.01 29.01 30.01 31.01'
)




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
    date = models.ForeignKey(Dates, on_delete=models.CASCADE, help_text="Data wykonania procedury.")

    def __str__(self):
        return self.procedure_name

