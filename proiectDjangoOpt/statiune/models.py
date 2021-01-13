from django.db import models

# Create your models here.
from django.db import models
#DataFlair Models

class Camera(models.Model):
    categ = (('da', 'cu baie'), ('nu', 'fara baie'))
    numar_camera = models.IntegerField(default=0)
    tip_camera = models.CharField(max_length=5, choices=categ)
    nr_persoane = models.IntegerField(default=0)

class RezervareCamere(models.Model):
    nume = models.CharField(max_length = 50);
    prenume = models.CharField(max_length = 50);
    telefon = models.CharField(max_length=10, default='07XXXXXXXX');
    adresaMail = models.EmailField(blank = True);
    check_in = models.DateTimeField();
    check_out = models.DateTimeField();
    numar_camere = models.IntegerField(default=0);
    camereRezervate = models.ManyToManyField(Camera)
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

class Restaurant(models.Model):
    numeRest = models.CharField(max_length = 50)
    specific = models.CharField(max_length = 30, default='type')
    adresa = models.CharField(max_length = 30, default='X street')
    telefonRest = models.CharField(max_length = 10, default='073XXXXXXX')
    descriereRest = models.CharField(max_length = 600, default='----')

    def __str__(self):
        return self.numeRest


class Transport(models.Model):
    rutaTrans = models.CharField(max_length = 80)
    tipTrans = models.CharField(max_length = 50)
    costTrans = models.CharField(max_length = 30)
    programTrans = models.CharField(max_length = 100, default='Nu este disponibil')
    contactTrans = models.CharField(max_length = 10, default='07XXXXXXXX')

    def __str__(self):
        return self.nume