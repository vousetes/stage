from django.contrib import admin
from .models import Cours

@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ['nom', 'enseignant', 'date_debut', 'date_fin']
    search_fields = ['nom', 'programme']

# Register your models here.
