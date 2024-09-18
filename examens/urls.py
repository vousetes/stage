from django.urls import path
from .views import( ajouter_examen,
                     liste_examen,examen_detail,
                     )

urlpatterns = [
    
    path('ajouter_examen/<int:cours_id>/', ajouter_examen, name='ajouter_examen'),

    path('liste_examens/<int:cours_id>/', liste_examen, name='liste_examens'), 
    path('examen_detail/<int:examen_id>/', examen_detail, name='examen_detail'), 
    
    
    
]
