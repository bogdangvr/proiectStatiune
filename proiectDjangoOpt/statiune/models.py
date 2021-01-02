from django.db import models

# Create your models here.
from django.db import models
#DataFlair Models
class Pensiune(models.Model):
    nume = models.CharField(max_length = 50)
    strada = models.CharField(max_length = 30, default='anonymous')
    adresaMail = models.EmailField(blank = True)
    telefon = models.CharField(max_length = 10, default='anonymous')
    descriere = models.CharField(max_length = 600, default='anonymous')
    def __str__(self):
        return self.nume

class Activitate(models.Model):
    tip = models.CharField(max_length = 50)
    varsta_minima = models.CharField(max_length = 30, default='Fara limita de varsta')
    sezon = models.CharField(max_length = 30, default='Toate')
    telefon = models.CharField(max_length = 10, default='Fara telefon')
    mail = models.EmailField(max_length = 30, default='Fara adresa de mail')
    def __str__(self):
        return self.nume