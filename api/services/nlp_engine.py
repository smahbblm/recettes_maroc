# Imports nécessaires :
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import pandas as pd
# from recettes.models import Recette

# Attributs de classe :
# - vectorizer : TfidfVectorizer pour transformer texte en vecteurs
# - recipe_vectors : Vecteurs TF-IDF de toutes les recettes
# - recipes_df : DataFrame avec toutes les recettes

# Méthode __init__() :
# - Charger toutes les recettes depuis Django
# - Créer corpus de texte (nom + description + ingrédients)
# - Entraîner TfidfVectorizer sur le corpus
# - Stocker les vecteurs des recettes

# Méthode find_similar_recipes(query, top_k=20) :
# - Transformer la requête utilisateur en vecteur TF-IDF
# - Calculer similarité cosinus avec tous les vecteurs recettes
# - Trier par score de similarité (descendant)
# - Retourner top_k recettes avec leurs scores
# - Format retour : [(recette_id, score), ...]

# Méthode _preprocess_text(text) :
# - Nettoyer le texte (minuscules, suppression accents)
# - Tokenisation basique
# - Retourner texte nettoyé
