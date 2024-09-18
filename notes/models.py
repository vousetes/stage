from django.db import models
from dashboard.models import Etudiant
from examens.models import Examen


class Note(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE, related_name="notes")
    note = models.FloatField()
    date_attribuee = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.etudiant.utilisateur.nom} - {self.examen.nom} : {self.note}"