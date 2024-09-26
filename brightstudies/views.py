from django.http.response import HttpResponse
from django.shortcuts import render
from dashboard.forms import EtudiantForm


def index(request):
    return render(request, "brightstudies/index.html")


def contact(request):
    return render(request, "brightstudies/contact.html")

def presentation(request):
    return render(request, "brightstudies/informations.html")

def apropos(request):

    return render(request, "brightstudies/apropos.html")

def services(request):
    return render(request, "brightstudies/services.html")

def insription_etudiant(request):
    form = EtudiantForm()
    return render(request, "auth/inscription-etudiant.html",{"form":form})

def login(request):
    return render(request, "auth/login.html")

def profil_etudiant_view(request):
    # Logique pour le profil étudiant
    return render(request, 'profil_etudiant.html')

def profil_enseignant_view(request):
    # Logique pour le profil enseignant
    return render(request, 'cours/profil_enseignant.html')
