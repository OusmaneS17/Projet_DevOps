from django.shortcuts import render, redirect
from django.http.response import HttpResponse, Http404
from .models import Contact, Newsletter
from inscription.models import Inscription
import mimetypes
import os

def Accueil_view(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        if type == "contact" :
            nom = request.POST.get('nom', '')
            prenom = request.POST.get('prenom', '')
            email = request.POST.get('email', '')
            objet = request.POST.get('objet', '')
            message = request.POST.get('message', '')
            # Enregistre les données dans la base de données
            contact = Contact(nom=nom, prenom=prenom, email=email, objet=objet, message=message)
            contact.save()
        elif type == "newsletter" :
            email = request.POST.get('email', '')
            # Enregistre les données dans la base de données
            newsletter = Newsletter(email=email)
            newsletter.save()
        
        return redirect('Soumissions')
    
    return render(request, 'accueil.html', locals())



