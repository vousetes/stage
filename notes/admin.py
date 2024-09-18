from django.contrib import admin
from .models import   Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['etudiant', 'examen', 'note', 'date_attribuee']  # Afficher ces champs dans la liste des notes
    search_fields = ['etudiant__nom', 'examen__nom']  # Permettre la recherche par nom d'étudiant ou d'examen


