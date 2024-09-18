from django.db import models
from cours.models import Cours

# Create your models here.
class Ressource(models.Model):
    TYPE_CHOICES = [
        ('document', 'Document'),
        ('lien', 'Lien'),
        ('video', 'Vidéo'),
       
    ]
    
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name="ressources")
    type_ressource = models.CharField(max_length=50, choices=TYPE_CHOICES)
    titre = models.CharField(max_length=255)
    fichier = models.FileField(upload_to='ressources/', blank=True, null=True)  # Pour les documents
    lien = models.URLField(blank=True, null=True)  # Pour les liens ou vidéos
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.titre} - {self.cours.nom}"