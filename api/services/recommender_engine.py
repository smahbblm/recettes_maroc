# Imports nécessaires :
# from .nlp_engine import NLPSearchEngine
# from .ml_engine import MLRecommendationEngine

# Attributs de classe :
# - nlp_engine : Instance NLPSearchEngine
# - ml_engine : Instance MLRecommendationEngine

# Méthode __init__() :
# - Initialiser nlp_engine
# - Initialiser ml_engine

# Méthode get_recommendations(user, query, top_n=10) :
# - Étape 1 : Utiliser NLP pour trouver recettes candidates
#   candidates = nlp_engine.find_similar_recipes(query, top_k=50)
# - Étape 2 : Utiliser ML pour personnaliser
#   ranked = ml_engine.rank_recipes(user, candidates)
# - Étape 3 : Combiner scores NLP + ML
#   score_final = 0.6 * score_ml + 0.4 * score_nlp
# - Étape 4 : Retourner top_n recettes finales
# - Format : [{'recette_id': id, 'score': score, 'recette': obj}, ...]

# Méthode _combine_scores(nlp_scores, ml_scores) :
# - Normaliser les scores (0-1)
# - Appliquer pondération
# - Retourner scores combinés
