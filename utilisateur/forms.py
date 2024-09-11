from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import utilisateur

class UtilisateurCreationFrom(UserCreationForm):
    class Meta:
        model = utilisateur
        fields =('email',)


class UtilisateurChangeForm(UserChangeForm):
    class Meta:
        model = utilisateur
        fields = ('email',)
