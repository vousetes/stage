from django.http.response import HttpResponse
from django.shortcuts import render
from dashboard.forms import EtudiantForm


def index(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")

def presentation(request):
    return render(request, "informations.html")

def apropos(request):

    return render(request, "apropos.html")

def services(request):
    return render(request, "services.html")

def insription_etudiant(request):
    form = EtudiantForm()
    return render(request, "inscription-etudiant.html",{"form":form})