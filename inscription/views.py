from django.shortcuts import render, redirect
from .models import Inscription
from home.models import Newsletter
def inscription_view(request):
    if request.method == 'POST':
        ecole = request.POST.get('ecole')
        membre1 = request.POST.get('membre1')
        classe1 = request.POST.get('classe1')
        membre2 = request.POST.get('membre2')
        classe2 = request.POST.get('classe2')
        membre3 = request.POST.get('membre3')
        classe3 = request.POST.get('classe3')
        email = request.POST.get('email')
        theme = request.POST.get('theme')
        article = request.FILES.get('article')
        # Enregistre les données dans la base de données
        inscription = Inscription(ecole=ecole, membre1=membre1, classe1=classe1, membre2=membre2, classe2=classe2, membre3=membre3, classe3=classe3, email=email, theme=theme, article = article)
        inscription.save()
        return redirect('Soumissions')
    return render(request, 'inscription/inscription.html')

