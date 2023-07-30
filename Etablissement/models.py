from django.db import models
from auditlog.models import AuditlogHistoryField

class Etablissement(models.Model):
    Id = models.AutoField(primary_key=True,default=None)
    Nom_Etab = models.CharField(max_length=200, unique=True, null=True)
    Adresse = models.CharField(max_length=200, null=True)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    history = AuditlogHistoryField()  # Champ pour stocker l'historique des modifications
  
    def __str__(self):
      return self.Nom_Etab

