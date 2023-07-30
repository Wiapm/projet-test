from django.forms import ModelForm
from .models import Equipement

class EquipementForm(ModelForm):
    class Meta:
        model=Equipement
        fields='__all__'