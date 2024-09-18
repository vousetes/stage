from django import forms
from .models import Note
from utilisateur.models import utilisateur



class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['etudiant', 'note'] 