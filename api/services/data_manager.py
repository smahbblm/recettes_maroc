# Imports nécessaires :
# from interactions.models import Favori, Evaluation, HistoriqueConsultation
# from preferences.models import (vos modèles de préférences)
# from account.models import ProfilUtilisateur

# Méthode get_user_preferences(user) :
# - Récupérer préférences explicites (région, niveau, allergies)
# - Retourner dictionnaire : {'region_pref': 'Fès', 'niveau': 'débutant'}

# Méthode get_user_interactions(user) :
# - Récupérer favoris de l'utilisateur
# - Récupérer évaluations (notes données)
# - Récupérer historique consultations
# - Calculer statistiques : note moyenne, catégories préférées
# - Retourner dictionnaire complet

# Méthode extract_user_features(user) :
# - Combiner préférences + interactions
# - Créer vecteur de features pour ML :
#   * Age utilisateur
#   * Région préférée (encodé)
#   * Niveau cuisine (encodé)
#   * Note moyenne donnée
#   * Nombre de favoris
#   * Catégories les plus consultées
# - Retourner array numpy normalisé

# Méthode get_recipe_interactions(recipe_id) :
# - Statistiques globales sur une recette
# - Note moyenne, nombre de favoris, popularité
# - Utilisé pour features recette
