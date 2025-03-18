from django.contrib import admin 
from django.urls import path, include 
from . import views 
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.Accueil_view, name = 'Accueil'),
    path('Soumissions/', include('Soumissions.urls')),
    path('inscription/', include('inscription.urls'))
]
