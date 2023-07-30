
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Equipement.urls')),
    path('Laboratoire/',include('Laboratoire.urls')),
    path('Etablissement/',include('Etablissement.urls')),
    path('Visiteur/',include('Visiteur.urls')),
    path('compte/',include('compte.urls')),
]
