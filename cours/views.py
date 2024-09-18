from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CoursForm
from .models import Cours

from ressource.models import Ressource
from examens.models import Examen  # Utilisez examens.models si Examen est défini là-bas



@login_required
@user_passes_test(lambda u: u.type_utilisateur == 'Enseignant')
def ajouter_cours(request):
    if request.method == 'POST':
        form = CoursForm(request.POST, request.FILES, user=request.user)  # Passer l'utilisateur connecté
        if form.is_valid():
            cours = form.save(commit=False)
            cours.enseignant = request.user  # Associer l'enseignant connecté au cours
            cours.save()
            return redirect('cours_liste')  # Redirection vers le profil enseignant
    else:
        form = CoursForm(user=request.user)  # Passer l'utilisateur connecté

    return render(request, 'ajouter_cours.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.type_utilisateur == 'Enseignant')
def liste_cours_par_programme(request):
    # Lister tous les cours, car seul un enseignant peut voir cette vue
    cours = Cours.objects.all()
    
    return render(request, 'cours_liste.html', {'cours': cours})


@login_required
@user_passes_test(lambda u: u.type_utilisateur == 'Enseignant')
def modifier_cours(request, cours_id):
    cours = get_object_or_404(Cours, id=cours_id)
    
    if request.method == 'POST':
        form = CoursForm(request.POST,request.FILES, instance=cours)
        if form.is_valid():
            form.save()
            return redirect('cours_liste')
    else:
        form = CoursForm(instance=cours)
    
    return render(request, 'modifier_cours.html', {'form': form, 'cours': cours})

@login_required
@user_passes_test(lambda u: u.type_utilisateur == 'Enseignant')
def supprimer_cours(request, cours_id):
    cours = get_object_or_404(Cours, id=cours_id)
    
    if request.method == 'POST':
        cours.delete()
        return HttpResponseRedirect(reverse('cours_liste'))  # Redirige vers la liste des cours
    
    return render(request, 'supprimer_cours.html', {'cours': cours})


@login_required
@user_passes_test(lambda u: u.type_utilisateur == 'Enseignant')
def profil_enseignant_view(request):
    # Récupérer les cours associés à l'enseignant connecté
    cours = Cours.objects.filter(enseignant=request.user)

    # Dictionnaire pour stocker les examens par cours
    examens_par_cours = {}
    
    # Pour chaque cours, récupérer les examens correspondants
    for c in cours:
        examens_par_cours[str(c.id)] = Examen.objects.filter(cours=c)
    
    return render(request, 'profil_enseignant.html', {
        'cours': cours,
        'examens_par_cours': examens_par_cours,  # Passer le dictionnaire au template
    })

@login_required
@user_passes_test(lambda u: u.type_utilisateur == 'Enseignant')
def cours_detail(request, cours_id):
    cours = get_object_or_404(Cours, id=cours_id)
    ressources = Ressource.objects.filter(cours=cours)

    return render(request, 'cours_detail.html', {'cours': cours, 'ressources': ressources})
