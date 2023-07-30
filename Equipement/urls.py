
from django.urls import path
from . import views
urlpatterns = [
    path('',views.accueil),
    path('map/',views.map,name='map'),
    path('ajouter/', views.ajouter_equipement, name='ajouter_equipement'),
    path('import-csv/', views.import_csv, name='import_csv'),
    path('showEquipement/', views.showEquipement, name='showEquipement'),
    path('supprimer_equipement/<str:pk>', views.supprimer_equipement, name='supprimer_equipement'),
    path('search/', views.search_equipments, name='search_equipments'),
    path('equipements/<int:equipement_id>/modifier/', views.modifier_etat, name='modifier_etat'),
]
