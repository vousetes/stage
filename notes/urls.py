from django.urls import path
from .views import( 
                     attribuer_notes)

urlpatterns = [
    
    path('attribuer_notes/<int:examen_id>/', attribuer_notes, name='attribuer_notes'),
   
    
]
