from django.contrib.auth.forms import UserCreationForm, UserChangeForm,  AuthenticationForm
from .models import utilisateur
from django import forms

class UtilisateurCreationFrom(UserCreationForm):
    class Meta:
        model = utilisateur
        fields =('email',)


class UtilisateurChangeForm(UserChangeForm):
    class Meta:
        model = utilisateur
        fields = ('email',)



class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={"class": "form-control"}))