from django.db import models
from cours.models import Cours

class Examen(models.Model):
    nom = models.CharField(max_length=255)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name='examens')
    date = models.DateField()

    def __str__(self):
        return f"{self.nom} - {self.cours.nom}"
# Create your models here.
