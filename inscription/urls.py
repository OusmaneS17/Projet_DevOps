from django.contrib import admin 
from django.urls import path 
from . import views # Du dossier local, importe views
urlpatterns = [
    path('', views.inscription_view, name='inscription'),
   
    
]