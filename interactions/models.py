"""from django.db import models
from django.conf import settings
# Importez le modèle Recette depuis l'application 'recettes'
from recettes.models import Recette

# --- 1. Modèle Favori (Intérêt Explicite Fort) ---
class Favori(models.Model):
    """
    Enregistre les recettes que l'utilisateur a mises en favori.
    C'est une donnée d'intérêt explicite utilisée par l'algorithme de recommandation.
    """
    
    # Lien vers l'utilisateur (le 'Qui')
    # settings.AUTH_USER_MODEL référence le modèle User par défaut de Django
    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='favoris' # Permet d'accéder aux favoris depuis l'utilisateur (ex: user.favoris.all())
    )
    
    # Lien vers la Recette (le 'Quoi')
    recette = models.ForeignKey(
        Recette, 
        on_delete=models.CASCADE,
        related_name='favori_set'
    )
    
    # Quand l'action a eu lieu
    date_ajout = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.utilisateur.username} a mis {self.recette.nom} en favori"
        
    class Meta:
        # Assure qu'un utilisateur ne peut ajouter une recette qu'une seule fois à ses favoris
        unique_together = ('utilisateur', 'recette')
        verbose_name_plural = "Favoris"


# --- 2. Modèle HistoriqueConsultation (Intérêt Implicite) ---
class HistoriqueConsultation(models.Model):
    """
    Enregistre chaque fois qu'un utilisateur consulte une recette.
    C'est une donnée d'intérêt implicite utilisée pour pondérer les recommandations récentes.
    """
    
    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='consultations'
    )
    
    recette = models.ForeignKey(
        Recette, 
        on_delete=models.CASCADE,
        related_name='consultation_set'
    )
    
    # Enregistre le moment de la consultation
    date_consultation = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.utilisateur.username} a consulté {self.recette.nom} le {self.date_consultation.strftime('%Y-%m-%d %H:%M')}"
        
    class Meta:
        # Trié par ordre décroissant (le plus récent en premier)
        ordering = ['-date_consultation']
        verbose_name_plural = "Historiques de Consultation"


# --- 3. Modèle Évaluation (Intérêt Explicite Qualitatif) ---
class Evaluation(models.Model):
    """
    Enregistre la note donnée par un utilisateur à une recette.
    Crucial pour l'analyse de qualité et l'éventuel filtrage collaboratif.
    """
    
    # Définition des choix de notes de 1 à 5
    NOTE_CHOICES = [(i, str(i)) for i in range(1, 6)]

    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='evaluations'
    )
    
    recette = models.ForeignKey(
        Recette, 
        on_delete=models.CASCADE,
        related_name='evaluation_set'
    )
    
    # Champ pour la note, restreint aux choix de 1 à 5
    note = models.IntegerField(choices=NOTE_CHOICES)
    
    # Quand l'évaluation a été donnée
    date_evaluation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.utilisateur.username} a noté {self.recette.nom}: {self.note}/5"
        
    class Meta:
        # Un utilisateur ne peut donner qu'une seule note par recette
        unique_together = ('utilisateur', 'recette')
        verbose_name_plural = "Évaluations"

        """