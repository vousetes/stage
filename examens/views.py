from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExamenForm
from .models import Cours, Examen 
from notes.models import Note




@login_required
@user_passes_test(lambda u: u.type_utilisateur == 'Enseignant')
def ajouter_examen(request, cours_id):
    if request.method == 'POST':
        form = ExamenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cours_liste')
    else:
        form = ExamenForm(initial={'cours': cours_id})
    
    return render(request, 'ajouter_examen.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.type_utilisateur == 'Enseignant')
def liste_examen(request, cours_id):
    # Récupérer le cours avec l'ID donné
    cours = get_object_or_404(Cours, id=cours_id)

    # Récupérer tous les examens associés à ce cours
    examens = Examen.objects.filter(cours=cours)
    
    return render(request, 'liste_examen.html', {'cours': cours, 'examens': examens})


@login_required
@user_passes_test(lambda u: u.type_utilisateur == 'Enseignant')
def examen_detail(request, examen_id):
    examen = Examen.objects.get(id=examen_id)
    notes = Note.objects.filter(examen=examen)  # Obtenir les notes associées à cet examen
    return render(request, 'examen_detail.html', {'examen': examen, 'notes': notes})

