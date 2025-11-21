# la définition de la classe Ingriends :

from django.db import models
class Produits(models.Model):

    nom                        = models.TextField()
    Categorie                  = models.TextField()
    Disponibitile_saisonnière  = models.TextField()
