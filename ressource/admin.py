from django.contrib import admin
from .models import  Ressource


@admin.register(Ressource)
class RessourceAdmin(admin.ModelAdmin):
    list_display = ['titre', 'cours', 'type_ressource', 'lien', 'fichier']
    search_fields = ['titre', 'cours__nom']  # Permet de rechercher par titre et cours
    list_filter = ['type_ressource']  # Permet de filtrer par type de ressource