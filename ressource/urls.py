from django.urls import path
from .views import( 
                     ajouter_ressource)

urlpatterns = [
    
    path('<int:cours_id>/ajouter_ressource/', ajouter_ressource, name='ajouter_ressource'),
    
    
]
