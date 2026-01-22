from django.db import models



class Osoba(models.Model):
    imie = models.CharField(max_length=50, help_text="Imię osoby.")
    nazwisko = models.CharField(max_length=50, help_text="Nazwisko osoby.")
    stanowisko = models.CharField(max_length=100, help_text="Stanowisko osoby w organizacji.")
    data_dodania = models.DateTimeField(auto_now_add=True, help_text="Data dodania rekordu.")

    def __str__(self):
        return f"{self.imie} {self.nazwisko} - {self.stanowisko}"


class Lekarz(models.Model):
    Imie = models.CharField(max_length=50, help_text="Imię lekarza.")
    Nazwisko = models.CharField(max_length=50, help_text="Nazwisko lekarza.")
    Specjalizacja = models.CharField(max_length=100, help_text="Specjalizacja lekarza.")

    def __str__(self):
        return f"{self.Imie} {self.Nazwisko} - {self.Specjalizacja}"
    

class Zabiegi(models.Model):
    nazwa_zabiegu = models.CharField(max_length=100, help_text="Nazwa procedury medycznej.")
    opis = models.TextField(help_text="Opis procedury medycznej.")
    koszt = models.DecimalField(max_digits=10, decimal_places=2, help_text="Koszt procedury medycznej.")
    lekarz = models.ForeignKey(Lekarz, on_delete=models.CASCADE, help_text="Lekarz wykonujący procedurę.")
    data = models.DateTimeField(help_text="Data i czas wykonania procedury.")

    def __str__(self):
        return self.nazwa_zabiegu

class Pacjent(models.Model):
    Imie = models.CharField(max_length=50, help_text="Imię pacjenta.")
    Nazwisko = models.CharField(max_length=50, help_text="Nazwisko pacjenta.")
    data_urodzenia = models.DateField(help_text="Data urodzenia pacjenta.")
    id_pacjenta = models.CharField(max_length=20, unique=True, help_text="pesel pacjenta.")
    email_pacjenta = models.EmailField(help_text="Email pacjenta.")

    def __str__(self):
        return f"{self.Imie} {self.Nazwisko} - {self.id_pacjenta}"