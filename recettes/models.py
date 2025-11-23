# recettes/models.py

from django.db import models

# --- 1. Tables de Référence : Region et Categorie  ---

class Region(models.Model):
    """Dictionnaire des régions d'origine (ex: Fès, Marrakech) pour le filtrage."""
    nom = models.CharField(max_length=100, unique=True)
    
    #===Pour affiché le nom de la region====
    def __str__(self):
        return self.nom
    #===cette classe est utilisable par django pourgèrere leur interface administrateur
    class Meta:
        verbose_name_plural = "Régions"

class Categorie(models.Model):
    """Dictionnaire des types de plats (ex: Plats Principaux, Desserts)."""
    nom = models.CharField(max_length=100, unique=True)
    
    #===l'affichage personalisé
    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name_plural = "Catégories"


class Ingredient(models.Model):
    """Dictionnaire de tous les ingrédients possibles."""
    nom = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nom
        
    class Meta:
        ordering = ['nom'] # Aide à la recherche dans l'admin
        verbose_name_plural = "Ingrédients"

# --- 2. Modèle Intermédiaire : QuantiteIngredient ---

class QuantiteIngredient(models.Model):
    """Table de liaison pour définir la quantité d'un ingrédient dans une recette."""
    recette = models.ForeignKey('Recette', on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantite = models.CharField(max_length=50, help_text="Ex: 200g, 1 cuillère à café")

    class Meta:
        unique_together = ('recette', 'ingredient') 
        verbose_name_plural = "Quantités d'Ingrédients"

# --- 3. Modèle Principal : Recette ---

class Recette(models.Model):
    """Modèle central du catalogue de recettes."""
    
    NIVEAU_CHOICES = [
        ('FACILE', 'Facile'),
        ('MOYEN', 'Moyen'),
        ('DIFFICILE', 'Difficile'),
    ]

    nom = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    instructions = models.TextField(default="Étapes de préparation détaillées.")
    image = models.ImageField(upload_to='recettes_images/', blank=True, null=True)
    
    # Métadonnées pour le Moteur (Attributs pour l'analyse)
    temps_preparation = models.IntegerField(help_text="En minutes")
    temps_cuisson = models.IntegerField(help_text="En minutes")
    niveau = models.CharField(max_length=10, choices=NIVEAU_CHOICES, default='SIMLE')
    
    # Relations One-to-Many
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    
    # Relation Many-to-Many via QuantiteIngredient
    ingredients = models.ManyToManyField(Ingredient, through=QuantiteIngredient)
    
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Non: " + self.nom + " descri^ption: " + self.description + " catégorie: " +  self.description 
        
    class Meta:
        verbose_name_plural = "Recettes"