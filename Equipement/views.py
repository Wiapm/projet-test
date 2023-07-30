from django.http import HttpResponse
import csv
import os
from Equipement.filters import EquipementFiltre
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Equipement
from Laboratoire.models import Laboratoire
from Visiteur.models import Visiteur
from .forms import EquipementForm
from Etablissement.models import Etablissement
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='connexion')
def accueil(request):
    equipements = Equipement.objects.all()
    laboratoires= Laboratoire.objects.all()
    visiteurs = Visiteur.objects.all()
    total_equipements = equipements.count()
    total_laboratoires= laboratoires.count()
    total_visiteurs = visiteurs.count() 
    derniers_equipements = equipements.order_by('-Date_Acquisition')[:3]
 

    context = {
        'total_equipements': total_equipements,
        'total_laboratoires': total_laboratoires,
        'equipements': equipements,
        'derniers_equipements': derniers_equipements,
        'visiteurs':visiteurs,
        'total_visiteurs': total_visiteurs,
    }
    return render(request, 'Equipement/dashboard.html', context)




@login_required(login_url='connexion')

def showEquipement(request):
    equipements = Equipement.objects.all()

    # Récupérer toutes les marques distinctes existantes
    marques_distinctes = Equipement.objects.values_list('Marque', flat=True).distinct()

    context = {
        'equipements': equipements,
        'marques_distinctes': marques_distinctes,
    }

    return render(request, 'Equipement/xmateriel.html', context)


@login_required(login_url='connexion')
def map(request):
    return render(request,'Equipement/map.html')

@login_required(login_url='connexion')   
def import_csv(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        file_extension = csv_file.name.split('.')[-1]
        if file_extension.lower() != 'csv':
            # Ajoutez un message d'erreur si l'extension n'est pas valide
            messages.error(request, "L'extension du fichier n'est pas valide. Veuillez sélectionner un fichier CSV.")
            return render(request, 'Equipement/import_csv.html')

        try:
            decoded_file = csv_file.read().decode('iso-8859-1')  # Utilisez l'encodage ISO-8859-1 (latin-1) pour lire le fichier CSV
            csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')

            for row in csv_data:
                # Vérifiez que toutes les données nécessaires sont présentes dans la ligne du CSV
                if len(row) >= 13:
                    # Récupérez les données de chaque colonne
                    reference = row[0]
                    etat = row[1]
                    marque = row[2]
                    date_acquisition = row[3]
                    laboratoire_name = row[4]
                    localisation = row[5]
                    telephone = row[6]
                    email = row[7]
                    abrv = row[8]
                    etablissement_name = row[9]
                    adresse = row[10]
                    etablissement_telephone = row[11]
                    etablissement_email = row[12]

                    # Recherchez l'établissement correspondant dans la base de données en utilisant le nom de l'établissement
                    try:
                        etablissement = Etablissement.objects.get(Nom_Etab=etablissement_name)
                    except Etablissement.DoesNotExist:
                        # Si l'établissement n'existe pas, créez-le et enregistrez-le dans la base de données
                        etablissement = Etablissement.objects.create(
                            Nom_Etab=etablissement_name,
                            Adresse=adresse,
                            telephone=etablissement_telephone,
                            email=etablissement_email
                        )
                    
                    # Vérifiez si le laboratoire existe déjà dans la base de données
                    laboratoire_exists = Laboratoire.objects.filter(Nom_Lab=laboratoire_name).exists()
                    if laboratoire_exists:
                        messages.warning(request, f"Le laboratoire '{laboratoire_name}' existe déjà dans la base de données. Le laboratoire et l'équipement ne seront pas importés.")
                        continue

                    # Créez une instance de Laboratoire et enregistrez-la dans la base de données
                    laboratoire = Laboratoire.objects.create(
                        Nom_Lab=laboratoire_name,
                        Localisation=localisation,
                        Telephone=telephone,
                        Email=email,
                        Abrv=abrv,
                        Etablissement=etablissement
                    )

                    # Créez une instance d'Equipement et enregistrez-la dans la base de données
                    Equipement.objects.create(
                        Reference=reference,
                        Etat=etat,
                        Date_Acquisition=date_acquisition,
                        Marque=marque,
                        Laboratoire=laboratoire
                    )
        
            # Redirigez ou renvoyez une réponse appropriée en fonction de votre besoin
            messages.success(request, 'Importation CSV réussie.')
            return redirect('showEquipement')  # Remplacez 'showEquipement' par le nom de la vue que vous souhaitez afficher après l'importation réussie.

        except Exception as e:
            messages.error(request, 'Une erreur s\'est produite lors de l\'importation du fichier CSV. Veuillez vérifier le format et l\'encodage du fichier.')
            return render(request, 'Equipement/import_csv.html')

    return render(request, 'Equipement/import_csv.html')

@login_required(login_url='connexion')
def ajouter_equipement(request):
    form = EquipementForm()
    if request.method == 'POST': 
        form=EquipementForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('showEquipement')
    context={'form':form}
    return render(request, 'Equipement/ajouter_equipement.html',context)

@login_required(login_url='connexion')
def supprimer_equipement(request,pk):
    equipement=Equipement.objects.get(Reference=pk)
    if request.method == 'POST':
        equipement.delete()
        return redirect('showEquipement')
    context ={'item':equipement}
    return render(request,'Equipement/supprimer_equipement.html',context)

@login_required(login_url='connexion')
def search_equipments(request):
    search_query = request.GET.get('Marque')  
    equipements = Equipement.objects.all()

    if search_query:
        equipement_filter = EquipementFiltre(request.GET, queryset=equipements)
        equipements = equipement_filter.qs
    return render(request, 'Equipement/rechercher.html', {'equipements': equipements})

def modifier_etat(request, equipement_id):
    equipement = Equipement.objects.get(id=equipement_id)

    if request.method == 'POST':
        nouvel_etat = request.POST['nouvel_etat']
        equipement.Etat = nouvel_etat
        equipement.save()
        return redirect('showEquipement')
    
    return render(request, 'Equipement/modifier_etat.html', {'equipement': equipement})
