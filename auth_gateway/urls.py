
from django.contrib import admin
from django.urls import path
from .views import * 

app_name = "AuthGateway"



urlpatterns = [
    path("validate_inscription/",validate_inscription, name="validate_inscription"),
    path("login_view/", login_view, name="login_view")
   
]

    
