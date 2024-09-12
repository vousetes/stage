from django.shortcuts import render ,redirect
from django.http.request import HttpRequest
from dashboard.forms import EtudiantForm
from utilisateur.models import utilisateur
from dashboard.models import Etudiant

from django.contrib import messages



def validate_inscription(request: HttpRequest):
    if request.method == "POST":
        form = EtudiantForm(request.POST)
        if form.is_valid(): 
            data =form.cleaned_data
            couriel =data ["couriel"]
            nom =data["nom"]
            prenom =data["prenom"]
            motdepasse=data["motdepasse"]
            Birthday =data["Birthday"]
            Enrollement_date =data["Enrollement_date"]
            Semester =data["Semester"]
            Etudes_Programme=data["Etudes_Programme"]



            couriel= str(couriel).lower()

            try:
                utilisateurexiste = utilisateur.objects.get(email=couriel)
                messages.info(request,"un compte existe avec ce couriel")
                return redirect("inscription_etudiant")

            except:
                newutilisateur= utilisateur( nom =nom, prenom = prenom ,email = couriel,type_utilisateur="etudiant")
                newutilisateur.set_password(motdepasse)
                newutilisateur.save()
                newEtudiant = Etudiant()
                newEtudiant.utilisateur = newutilisateur
                newEtudiant.Birthday = str(Birthday)
                newEtudiant.Enrollement_date = str(Enrollement_date)
                newEtudiant.Semester = str(Semester)
                newEtudiant.Etudes_Programme = str(Etudes_Programme)
                newEtudiant.save()
                messages.success(request, "Votre inscription a été réussie")
                return redirect("inscription_etudiant")



        else:
            return render(request, "inscription_etudiant.html", {"form": form})



    else: 
        return redirect("inscription_etudiant")    


# Create your views here.
