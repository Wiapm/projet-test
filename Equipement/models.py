from django.db import models
from Laboratoire.models import Laboratoire
from auditlog.models import AuditlogHistoryField

class Equipement(models.Model):
    ETAT_CHOICES = (
        ('Installé', 'Installé'),
        ('en panne', 'En panne'),
        ('Fonctionnel', 'Fonctionnel')
    )
    CATEGORIE_CHOICES = (
    ('Chimie', 'Chimie'),
    ('Biologie', 'Biologie'),
    ('Microbiologie', 'Microbiologie'),
    ('Biotechnologie', 'Biotechnologie'),
    ('Autre', 'Autre')
)
    Reference = models.CharField(max_length=200, unique=True, null=True)
    Etat = models.CharField(max_length=200, null=True, choices=ETAT_CHOICES)
    Date_Acquisition = models.DateField(auto_now_add=True)
    Marque = models.CharField(max_length=200, null=True)
    Laboratoire = models.ForeignKey(Laboratoire, on_delete=models.CASCADE)
    Categorie = models.CharField(max_length=200, choices=CATEGORIE_CHOICES)  # Ajoutez ce champ
    history = AuditlogHistoryField()  
  
    def __str__(self):
        return self.Reference
