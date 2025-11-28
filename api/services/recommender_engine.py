from .nlp_engine import Nlp
from preferences.models import PreferenceUtilisateur
from interactions.models import Favori, Evaluation, HistoriqueConsultation

def get_user_preferences(user):
    try:
        prefs = user.preferences
        return {
            'categories_preferees': set(prefs.categories_preferees.values_list('nom', flat=True)),
            'regions_preferees': set(prefs.regions_preferees.values_list('nom', flat=True)),
            'ingredients_evites': set(prefs.ingredients_evites.values_list('nom', flat=True)),
        }
    except PreferenceUtilisateur.DoesNotExist:
        return {
            'categories_preferees': set(),
            'regions_preferees': set(),
            'ingredients_evites': set(),
        }

def get_user_interactions(user):
    favoris = set(Favori.objects.filter(utilisateur=user).values_list('recette__name', flat=True))
    notes_positives = set(Evaluation.objects.filter(utilisateur=user, note__gte=4).values_list('recette__name', flat=True))
    consultations = set(HistoriqueConsultation.objects.filter(utilisateur=user).values_list('recette__name', flat=True))

    return {
        'favoris': favoris,
        'notes_positives': notes_positives,
        'consultations': consultations,
    }

def filter_by_content(user, nlp_results):
    prefs = get_user_preferences(user)
    interactions = get_user_interactions(user)

    filtered = []

    for recette in nlp_results:
        name = recette.get("name", "")

        recette_ingredients = [i.strip().lower() for i in recette.get("ingredients", "").split("-")]

        if any(ing.lower() in prefs['ingredients_evites'] for ing in recette_ingredients):
            continue
        score = 1.0   # ou recette["score_nlp"] 
        if recette.get("category") in prefs['categories_preferees']:
            score += 0.5
        if recette.get("region") in prefs['regions_preferees']:
            score += 0.5
        if name in interactions['favoris']:
            score += 0.3
        if name in interactions['notes_positives']:
            score += 0.2
        if name in interactions['consultations']:
            score += 0.1
        recette['score_content'] = score
        filtered.append(recette)


    return sorted(filtered, key=lambda r: r['score_content'], reverse=True)