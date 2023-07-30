
from django.urls import path
from .views import activate  
from . import views

urlpatterns = [
    path('inscription',views.signup , name= 'inscription'),
    path('connexion',views.accesPage , name= 'connexion'),
    path('quitter',views.logoutUser, name='quitter'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        activate, name='activate'),  
]
