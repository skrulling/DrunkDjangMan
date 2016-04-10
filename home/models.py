from django.db import models

class Vare(models.Model):
    navn = models.CharField(max_length=250)
    pris = models.CharField(max_length=20)
    alkohol = models.CharField(max_length=10)
    volum = models.CharField(max_length=10)
    kalkulering = models.CharField(max_length=20)

    def __str__(self):
        return self.navn + ' - ' + self.kalkulering
