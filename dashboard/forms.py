from django import forms
from .models import Etudiant

class EtudiantForm(forms.ModelForm):
    nom = forms.CharField(max_length=255)
    prenom = forms.CharField(max_length=255)
    couriel = forms.EmailField()
    motdepasse= forms.CharField(widget=forms.PasswordInput(attrs={"type" : "password"}))

    class Meta:
        model = Etudiant
        fields = ["Birthday","Enrollement_date","Semester","Etudes_Programme"]








