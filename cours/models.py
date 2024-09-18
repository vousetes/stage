from django.db import models
from utilisateur.models import utilisateur
#from django.utils import timezone

PROGRAMME_CHOICES = [
    ('Bachelor', 'bachelor'),
    ('Master', 'master'),
    ('PhD', 'phd'),
    ('DEC', 'dec'),
    ('AEC', 'aec'),
]

NIVEAU_CHOICES = [
    ('1ere année', '1ère année'),
    ('2eme année', '2ème année'),
    ('3eme année', '3ème année'),
    ('4eme année', '4ème année'),
]

JOUR_CHOICES = [
    ('Lundi', 'Lundi'),
    ('Mardi', 'Mardi'),
    ('Mercredi', 'Mercredi'),
    ('Jeudi', 'Jeudi'),
    ('Vendredi', 'Vendredi'),
]

class Cours(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    programme = models.CharField(max_length=10, choices=PROGRAMME_CHOICES)
    niveau = models.CharField(max_length=10, choices=NIVEAU_CHOICES)
    credits = models.IntegerField()
    enseignant = models.ForeignKey(utilisateur, on_delete=models.CASCADE, limit_choices_to={'type_utilisateur': 'Enseignant'})
    date_debut = models.DateField()
    date_fin = models.DateField()
    prerequis = models.ManyToManyField('self', blank=True)
    jour = models.CharField(max_length=10, choices=JOUR_CHOICES)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    photo = models.ImageField(upload_to='cours_photos/', blank=True, null=True)  # Ajout du champ photo
    def __str__(self):
        return f"{self.nom} - {self.programme}"
    


