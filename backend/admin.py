from django.contrib import admin
from .models import *
# Register your models here.


class CategorieAdmin(admin.ModelAdmin):
    list_display = ("nom", "description") # pour l'affichage dans la database
admin.site.register(Categorie, CategorieAdmin) #

class ArticlePage(admin.ModelAdmin):
    list_display = ("nom", "prix", "quantite")
admin.site.register(Article, ArticlePage)


class VenteAdmin(admin.ModelAdmin):
    list_display = ("numero_facture", "date_vente", "quantite", "prix_unitaire")
admin.site.register(Vente, VenteAdmin)

class StockAdmin(admin.ModelAdmin):
    list_display = ("article", "quantite_disponible", "seuil_alerte", "date_derniere_entree", "date_derniere_sortie")
admin.site.register(Stock, StockAdmin)

