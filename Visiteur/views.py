from django.shortcuts import render
from .models import Visiteur 
# Create your views here.
def view_Graphic(request):
    
    return render(request, 'Equipement/dashboard.html')