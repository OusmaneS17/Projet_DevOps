from django.contrib import admin
from django.urls import path, re_path  # ✅ Utiliser re_path() au lieu de url()
from . import views  # Importer views du dossier local

urlpatterns = [
    path('', views.Soumissions_view, name='Soumissions'),
    re_path(r'^(?P<article_id>\d+)$', views.download_file, name='download_article'),  # ✅ Remplace url() par re_path()
]
