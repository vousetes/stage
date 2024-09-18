from django.contrib import admin
from .models import  Examen



@admin.register(Examen)
class ExamenAdmin(admin.ModelAdmin):
    list_display = ['nom', 'date', 'cours']  # Les champs à afficher dans la liste des examens
    search_fields = ['nom', 'cours__nom']  # Permettre la recherche par nom d'examen ou de cours
