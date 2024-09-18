"""
URL configuration for brightstudies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .views import * 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name= "index"),
    path('contact/', contact, name= "contact"),
    path('mes-info/', presentation, name= "mes-info"),
    path('apropos/', apropos, name= "apropos"),
    path('nos-services/', services, name= "nos-services"),
    path("inscription-etudiant/", insription_etudiant, name= "inscription_etudiant"),
    path("auth_gateway/", include("auth_gateway.urls")),
    path("login/", login, name="login"),

    path('profil/etudiant/', profil_etudiant_view, name='profil_etudiant'),
    path('profil/enseignant/', profil_enseignant_view, name='profil_enseignant'),
    path("logout/", LogoutView.as_view(), name="logout"),
   # path('gestion_cours/', include('gestion_cours.urls')),
    path('cours/', include('cours.urls')),
    path('notes/', include('notes.urls')),
    path('examens/', include('examens.urls')),
    path('ressource/', include('ressource.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


