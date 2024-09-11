from django.contrib import admin
from .models import utilisateur
from django.contrib.auth.admin import UserAdmin
from .forms import UtilisateurCreationFrom, UtilisateurChangeForm

# Register your models here.

class utilisateurAdmin(UserAdmin):
    add_form = UtilisateurCreationFrom
    form = UtilisateurChangeForm
    model = utilisateur

    list_display = ('email', 'nom','prenom', 'is_active','is_superuser','type_utilisateur')
    list_filter =('email', 'nom','prenom', 'is_active','is_superuser','type_utilisateur')

    fieldsets = (
        (None, {'fields': ('nom', 'prenom','email','password')}),
        ('Permissions', {'fields': ('type_utilisateur','is_staff', 'is_active', 'is_superuser',
                                   'groups', 'user_permissions')}), 
        
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
                    
            'fields': ('nom', 'prenom', 'email', 'password1', 'password2','type_utilisateur' ,'is_staff',
                       'is_active', 'is_superuser','groups', 'user_permissions'),
        }),
    )

    search_fields = ('email', )
    ordering = ('email',"type_utilisateur")


admin.site.register(utilisateur,utilisateurAdmin)