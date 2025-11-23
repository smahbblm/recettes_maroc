# interactions/models.py

from django.db import models
from django.conf import settings # Important pour la liaison au modèle User
from recettes.models import Recette # Liaison au catalogue de recettes

# --- 1. Favori ---

class Favori(models.Model):
    """Enregistre les recettes explicitement aimées par l'utilisateur."""
    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='favoris'
    )
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Un utilisateur ne peut pas mettre la même recette en favori deux fois
        unique_together = ('utilisateur', 'recette') 
        verbose_name_plural = "Favoris"

    def __str__(self):
        return f"{self.utilisateur.username} a mis en favori {self.recette.nom}"

# --- 2. HistoriqueConsultation ---

class HistoriqueConsultation(models.Model):
    """Enregistre chaque vue de recette pour déterminer l'intérêt récent."""
    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    date_consultation = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # Permet d'avoir plusieurs consultations de la même recette
        ordering = ['-date_consultation'] 
        verbose_name_plural = "Historiques de Consultation"

    def __str__(self):
        return f"{self.utilisateur.username} a consulté {self.recette.nom}"

# --- 3. Evaluation (Notation) ---

class Evaluation(models.Model):
    """Enregistre les notes données par l'utilisateur (ex: de 1 à 5)."""
    
    NOTE_CHOICES = [(i, i) for i in range(1, 6)] # Notes de 1 à 5

    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    note = models.IntegerField(choices=NOTE_CHOICES)
    date_evaluation = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Un utilisateur ne peut évaluer la même recette qu'une seule fois
        unique_together = ('utilisateur', 'recette') 
        verbose_name_plural = "Évaluations"

    def __str__(self):
        return f"{self.utilisateur.username} a noté {self.recette.nom} ({self.note}/5)"