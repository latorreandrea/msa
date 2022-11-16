from django.db import models
from django.urls import reverse

# Create your models here.
TIPOLOGIA = (
    ("fisso", "fisso"),
    ("portatile", "portalile"),
    ("dismesso", "dismesso"),
)

class Pc(models.Model):
    seriale = models.CharField(max_length=50)
    codice_interno = models.CharField(max_length=50)
    modello = models.CharField(max_length=254)
    installazione = models.DateField()
    tipologia = models.CharField(max_length=100,
                  choices=TIPOLOGIA, default=1)
    note = models.TextField(default="",blank=True)

    class Meta:
        verbose_name_plural = "Computer"

    def __str__(self):
        return self.tipologia + " seriale: " + self.seriale + " modello: " + self.modello

    def get_absolute_url(self):
        return reverse("dettaglio_pc", kwargs={"pk": self.pk})


class Telefono(models.Model):
    seriale = models.CharField(max_length=50)
    codice_interno = models.CharField(max_length=50)
    modello = models.CharField(max_length=254)
    assegnazione = models.DateField()    
    note = models.TextField(default="",blank=True)
    
    class Meta:
        verbose_name_plural = "Cellulari"

    def __str__(self):
        return self.modello + " seriale: " + self.seriale 

    def get_absolute_url(self):
        return reverse("dettaglio_telefono", kwargs={"pk": self.pk})



class Periferiche(models.Model):
    name = models.CharField(max_length=254)
    quantita = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
    
    def get_absolute_url(self):
        return reverse("dettaglio_periferiche", kwargs={"pk": self.pk})



