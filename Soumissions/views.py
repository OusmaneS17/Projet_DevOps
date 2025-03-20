from django.shortcuts import render, redirect
from inscription.models import Inscription
from home.models import Newsletter
from django.http.response import HttpResponse, Http404
import mimetypes
import os

def Soumissions_view(request):
    articles = Inscription.objects.all()

    return render(request,'Soumissions/Soumissions.html', {"articles" : articles})

from django.http import FileResponse
def view_file(response) :
    img = open(r'static\images\3hduj2.png', 'rb')
    response = FileResponse(img)
    return response


def download_file(request, article_id):
    #filename = "Rapport_de_stage_Y._MINTOAMA_VF.pdf"
    #filepath = r"media/article/Rapport_de_stage_Y._MINTOAMA_VF.pdf"
    filename = Inscription.objects.get(pk=article_id).article.name
    filepath  = Inscription.objects.get(pk=article_id).article.path

    # Open the file for reading content in binary mode
    with open(filepath, 'rb') as file:
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        
        # Set the return value of the HttpResponse
        response = HttpResponse(file.read(), content_type=mime_type)
        
        # Set the HTTP header for sending to the browser
        response['Content-Disposition'] = f"attachment; filename={filename}"
        
        # Return the response value
        return response
