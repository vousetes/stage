from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import utilisateurManager



UTILISATEUR_TYPES_CHOICES =(
    ("adminitration_menbre","Menbre d'administration"),
    ("Etudiant", "Etudiant"),
    ("Enseignant", "Enseignant"),
   

)


# Create your models here.


class utilisateur(AbstractBaseUser, PermissionsMixin):
    nom = models.CharField(_("Nom"),max_length=255)
    prenom = models.CharField(_("prenom"),max_length=255)
    email = models.EmailField(_("Couriel Personnel"),unique=True)
    type_utilisateur = models.CharField(max_length=255, choices=UTILISATEUR_TYPES_CHOICES,default="Etudiant")
    is_active = models.BooleanField(_("Compte Actif"),default=True)
    is_staff = models.BooleanField(default=False)

    objects = utilisateurManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom']

    class Meta:
        verbose_name = _("Utilisateur")
        verbose_name_plural = _("Utilisateurs")
