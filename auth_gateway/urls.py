
from django.contrib import admin
from django.urls import path
from .views import * 

app_name = "AuthGateway"



urlpatterns = [
    path("validate_inscription/",validate_inscription, name="validate_inscription")
    
]
