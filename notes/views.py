from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from .models import   Examen, Note
from django.shortcuts import get_object_or_404
from .forms import  NoteForm


@login_required
@user_passes_test(lambda u: u.type_utilisateur == 'Enseignant')
def attribuer_notes(request, examen_id):
    examen = get_object_or_404(Examen, id=examen_id)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)  # Ne pas enregistrer immédiatement pour ajouter l'examen
            note.examen = examen  # Associer l'examen
            note.save()  # Sauvegarder la note avec l'examen et l'étudiant
            return redirect('examen_detail', examen_id=examen.id)  # Redirection après la soumission
    else:
        form = NoteForm()  # Initialiser le formulaire sans l'étudiant
    
    return render(request, 'notes/attribuer_notes.html', {'examen': examen, 'form': form})