from django.db import models
from Etablissement.models import Etablissement
from auditlog.models import AuditlogHistoryField

# Create your models here.
class Laboratoire(models.Model):
    Nom_Lab = models.CharField(max_length=100, unique=True, null=True)
    Localisation = models.CharField(max_length=100)
    Telephone = models.CharField(max_length=20)
    Email = models.EmailField()
    Abrv = models.CharField(max_length=50)
    Etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE, default=None )
    history = AuditlogHistoryField()  # Champ pour stocker l'historique des modifications
    def __str__(self):
        return self.Nom_Lab
