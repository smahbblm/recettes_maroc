# account/models.py

from django.db import models
from django.conf import settings
from recettes.models import Region

# --- Modèle Principal : ProfilUtilisateur ---

class ProfilUtilisateur(models.Model):
    """Profil personnel étendu de l'utilisateur pour le système de recommandation."""
    
    NIVEAU_CHOICES = [
        ('DEBUTANT', 'Débutant'),
        ('INTERMEDIAIRE', 'Intermédiaire'),
        ('EXPERT', 'Expert'),
    ]
    
    # Liaison obligatoire avec l'utilisateur Django
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profil'
    )
    
    # Informations personnelles pour recommandations
    age = models.IntegerField(null=True, blank=True, help_text="Age de l'utilisateur")
    
    niveau_cuisine = models.CharField(
        max_length=15,
        choices=NIVEAU_CHOICES,
        default='DEBUTANT',
        help_text="Niveau de compétence en cuisine"
    )
    
    ville = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Ville de résidence"
    )
    
    region_origine = models.ForeignKey(
        Region,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Région d'origine culinaire"
    )
    
    # Photo de profil (optionnel)
    photo = models.ImageField(
        upload_to='profils/',
        null=True,
        blank=True,
        help_text="Photo de profil utilisateur"
    )
    
    # Bio courte
    bio = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        help_text="Description courte de l'utilisateur"
    )
    
    # Métadonnées
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Profils Utilisateurs"
    
    def __str__(self):
        return f"Profil de {self.user.username}"
    
    def get_full_name(self):
        """Retourne le nom complet si disponible, sinon username."""
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name}"
        return self.user.username
