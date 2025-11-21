# la définition de la classe Ingriends :

from django.db import models
class Ingredients(models.Model):

    nom                        = models.TextField()
    Categorie                  = models.TextField()
    Disponibitile_saisonnière  = models.TextField()
