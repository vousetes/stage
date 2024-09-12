from django.db import models
from utilisateur.models import utilisateur
from .constante import STUDIES_PROGRAM_NAME_CHOICES, ERILLEMENT_SEMESTER
# Create your models here.

class Enseignant(models.Model):
    utilisateur = models.OneToOneField(utilisateur, on_delete=models.CASCADE)
    grade = models.CharField(max_length=50)
    Expertise = models.CharField(max_length=255)
    Bio = models.CharField(max_length=  255)
    Code_proffessoral=models.CharField(max_length=255)

    def __str__(self) -> str:
        return "Compte Enseignant de " + self.utilisateur.prenom + " " + self.utilisateur.nom
    

class Etudiant(models.Model):
    utilisateur = models.OneToOneField(utilisateur, on_delete=models.CASCADE)
    Birthday = models.DateField()
    Enrollement_date =  models.DateField()
    Semester = models.CharField(max_length=255, choices=ERILLEMENT_SEMESTER, default="hiver")
    Etudes_Programme = models.CharField(max_length=255, choices=STUDIES_PROGRAM_NAME_CHOICES, default="Bachelor")
    code_permanent = models.CharField(max_length=255)

    def __str__(self) -> str:
        return "Compte Etudiant de " + self.utilisateur.prenom + " " + self.utilisateur.nom
    