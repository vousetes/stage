from django.contrib import admin
from .models import Enseignant, Etudiant
from django.core.mail import send_mail
from django.conf import settings


# Fonction d'envoi de l'e-mail à l'étudiant avec le mot de passe en texte clair
def send_email_etudiant(couriel, nom, enrollement_date, semester, etudes_programme, code_permanent, motdepasse):
    subject = 'Votre inscription à BrightStudies'
    message = f'Bonjour {nom},\n\nVoici vos informations d\'inscription :\n' \
              f'Date d\'enrôlement : {enrollement_date}\n' \
              f'Semestre : {semester}\n' \
              f'Programme d\'étude : {etudes_programme}\n' \
              f'Code permanent : {code_permanent}\n' \
              f'Mot de passe : {motdepasse}\n\nBienvenue sur BrightStudies !'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [couriel]
    send_mail(subject, message, email_from, recipient_list)

# Fonction d'envoi de l'e-mail au professeur avec le mot de passe en texte clair
def send_email_professeur(couriel, code_professoral, motdepasse):
    subject = 'Votre compte professeur sur BrightStudies'
    message = f'Bonjour,\n\nVoici vos informations d\'inscription :\n' \
              f'Courriel : {couriel}\n' \
              f'Code professoral : {code_professoral}\n' \
              f'Mot de passe : {motdepasse}\n\nBienvenue sur BrightStudies !'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [couriel]
    send_mail(subject, message, email_from, recipient_list)

# Admin pour Etudiant
@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'Enrollement_date', 'Semester', 'Etudes_Programme', 'code_permanent')

    # Surcharge de la méthode save_model pour envoyer un e-mail après l'enregistrement
    def save_model(self, request, obj, form, change):
        # Capturer le mot de passe avant qu'il ne soit haché
        motdepasse = form.cleaned_data.get('password')  # Capture du mot de passe avant hachage

        super().save_model(request, obj, form, change)

        couriel = obj.utilisateur.email
        nom = obj.utilisateur.nom
        enrollement_date = obj.Enrollement_date
        semester = obj.Semester
        etudes_programme = obj.Etudes_Programme
        code_permanent = obj.code_permanent

        # Envoi de l'e-mail à l'étudiant avec le mot de passe en clair
        send_email_etudiant(couriel, nom, enrollement_date, semester, etudes_programme, code_permanent, motdepasse)

# Admin pour Enseignant
@admin.register(Enseignant)
class EnseignantAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'grade', 'Code_proffessoral')

    # Surcharge de la méthode save_model pour envoyer un e-mail après l'enregistrement
    def save_model(self, request, obj, form, change):
        # Capturer le mot de passe avant qu'il ne soit haché
        motdepasse = form.cleaned_data.get('password')  # Capture du mot de passe avant hachage

        super().save_model(request, obj, form, change)

        couriel = obj.utilisateur.email
        code_professoral = obj.Code_proffessoral

        # Envoi de l'e-mail au professeur avec le mot de passe en clair
        send_email_professeur(couriel, code_professoral, motdepasse)
