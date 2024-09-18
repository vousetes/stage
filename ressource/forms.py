from django import forms

from .models import  Ressource

class RessourceForm(forms.ModelForm):
    class Meta:
        model = Ressource
        fields = ['type_ressource', 'titre', 'fichier', 'lien', 'description']
        
    def clean(self):
        cleaned_data = super().clean()
        fichier = cleaned_data.get("fichier")
        lien = cleaned_data.get("lien")

        # Si ni fichier ni lien n'est fourni, lever une erreur
        if not fichier and not lien:
            raise forms.ValidationError("Vous devez fournir un fichier ou un lien.")
        
        return cleaned_data
