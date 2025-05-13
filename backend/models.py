from django.db import models

# Create your models here.
 
class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField(null=True, blank=True)

class Article(models.Model):
    nom = models.CharField(max_length=100, unique=True, null=False)
    prix = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    quantite = models.IntegerField(null=False)

    def __str__(self):
        return self.nom
class Vente(models.Model):
    numero_facture = models.CharField(max_length=100, unique=True)
    date_vente = models.DateTimeField(auto_now_add=True)
    quantite = models.PositiveIntegerField(null=False)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.numero_facture

class Stock(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    quantite_disponible = models.PositiveIntegerField()
    seuil_alerte = models.PositiveIntegerField(default=10)
    date_derniere_entree = models.DateTimeField(null=True, blank=True)
    date_derniere_sortie = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.produit.nom} - {self.quantite_disponible} en stock"