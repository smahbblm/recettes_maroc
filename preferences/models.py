# preferences/models.py

from django.db import models
from django.conf import settings
from recettes.models import Categorie, Region, Ingredient

# --- Modèle Principal : PreferenceUtilisateur ---

class PreferenceUtilisateur(models.Model):
    """Préférences culinaires explicites de l'utilisateur pour le système de recommandation."""
    
    # Liaison obligatoire avec l'utilisateur Django
    utilisateur = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='preferences'
    )
    
    # Préférences culinaires
    categories_preferees = models.ManyToManyField(
        Categorie,
        blank=True,
        help_text="Types de plats préférés (ex: Plats Principaux, Desserts)"
    )
    
    regions_preferees = models.ManyToManyField(
        Region,
        blank=True,
        help_text="Régions culinaires préférées (ex: Fès, Marrakech)"
    )
    
    ingredients_evites = models.ManyToManyField(
        Ingredient,
        blank=True,
        help_text="Ingrédients à éviter (allergies, restrictions alimentaires)"
    )
    
    # Métadonnées
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Préférences Utilisateurs"
    
    def __str__(self):
        return f"Préférences de {self.utilisateur.username}"
