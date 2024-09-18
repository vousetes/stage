from django.urls import path
from .views import( ajouter_cours, liste_cours_par_programme, 
                   profil_enseignant_view, modifier_cours, 
                   supprimer_cours
                     ,cours_detail)

urlpatterns = [
    path('ajouter/', ajouter_cours, name='ajouter_cours'),
    path('', liste_cours_par_programme, name='cours_liste'),
    path('profil_enseignant/', profil_enseignant_view, name='profil_enseignant'),
     path('<int:cours_id>/modifier/', modifier_cours, name='modifier_cours'),
    path('<int:cours_id>/supprimer/', supprimer_cours, name='supprimer_cours'),
    path('<int:cours_id>/', cours_detail, name='cours_detail'),

    
]
