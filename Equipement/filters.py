import django_filters
from .models import Equipement 

class EquipementFiltre(django_filters.FilterSet):
    Marque = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Equipement
        fields = ['Marque']
