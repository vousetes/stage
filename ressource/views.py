from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .forms import RessourceForm
from .models import Ressource, Cours
from django.shortcuts import get_object_or_404

 

@login_required
@user_passes_test(lambda u: u.type_utilisateur == 'Enseignant')
def ajouter_ressource(request, cours_id):
    cours = get_object_or_404(Cours, id=cours_id)
    
    if request.method == 'POST':
        form = RessourceForm(request.POST, request.FILES)
        if form.is_valid():
            ressource = form.save(commit=False)
            ressource.cours = cours  # Associe la ressource au cours
            ressource.save()
            return redirect('cours_detail', cours_id=cours.id)  # Redirige vers la page des détails du cours
    else:
        form = RessourceForm()

    return render(request, 'ajouter_ressource.html', {'form': form, 'cours': cours})
