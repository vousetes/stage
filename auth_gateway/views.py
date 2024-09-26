from django.shortcuts import render ,redirect
from django.http.request import HttpRequest
from dashboard.forms import EtudiantForm
from utilisateur.models import utilisateur
from dashboard.models import Etudiant
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login
from .forms import CustomLoginForm



from django.contrib import messages

# Fonction d'envoi de l'email
def send_confirmation_email(couriel, nom):
    subject = 'Confirmation de votre inscription'
    message = f'Bonjour {nom},\n\nVotre admission a été envoyer ! Veillez atttendre vos identifiant de la part de BrightStudies.'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [couriel]
    send_mail(subject, message, email_from, recipient_list)



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

                send_confirmation_email(couriel, nom)
                messages.success(request, "Votre admission a été envoyer avec success")
                return redirect("inscription_etudiant")



        else:
            return render(request, "auth/inscription-etudiant.html", {"form": form})



    else: 
        return redirect("inscription_etudiant") 




def login_view(request):
    # Récupère le type d'utilisateur depuis GET ou POST
    user_type = request.POST.get('type') or request.GET.get('type')

    if request.method == "POST":
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)

            if user is not None:
                # Vérifie si le type d'utilisateur est correct
                print(f"Utilisateur connecté : {user.email} - Type : {user.type_utilisateur}")

                # Empêcher un enseignant de se connecter en tant qu'étudiant et vice versa
                if user_type == "Etudiant" and user.type_utilisateur != "Etudiant":
                    messages.error(request, "Vous avez sélectionné 'Étudiant', mais votre compte est enregistré comme Enseignant.")
                    return redirect("login")
                if user_type == "Enseignant" and user.type_utilisateur != "Enseignant":
                    messages.error(request, "Vous avez sélectionné 'Enseignant', mais votre compte est enregistré comme Étudiant.")
                    return redirect("login")

                # Si tout est correct, connecter l'utilisateur
                login(request, user)
                print("Connexion réussie")
                
                # Rediriger vers la bonne page de profil
                if user.type_utilisateur == "Etudiant":
                    return redirect("profil_etudiant")
                elif user.type_utilisateur == "Enseignant":
                    return redirect("profil_enseignant")

    else:
        form = CustomLoginForm()

    return render(request, "auth/login.html", {"form": form})
