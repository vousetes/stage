from django import forms
from .models import Cours


class CoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = ['nom', 'description', 'programme', 'niveau', 'credits', 'date_debut', 'date_fin', 'jour', 'heure_debut', 'heure_fin', 'photo']  # Supprimer le champ 'enseignant'
    
    def __init__(self, *args, **kwargs):
        # Prendre en compte l'utilisateur
        self.user = kwargs.pop('user', None)
        super(CoursForm, self).__init__(*args, **kwargs)
        
        # Afficher le nom de l'enseignant connecté
        if self.user and self.user.type_utilisateur == 'Enseignant':
            self.fields['enseignant_label'] = forms.CharField(
                label="Enseignant",
                initial=f"{self.user.nom} {self.user.prenom}",
                widget=forms.TextInput(attrs={'readonly': 'readonly'})
            )
