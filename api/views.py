print("🔵 Début du chargement de api/views.py")
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .services.recommender_engine import filter_by_content
from .services.nlp_engine import Nlp
import math
import json

print("✅ Imports terminés")

_nlp_engine_cache = None

def get_nlp_engine():
    global _nlp_engine_cache
    #if _nlp_engine_cache is None:
    print("🔄 Chargement du moteur NLP... (cela peut prendre quelques minutes)")
    _nlp_engine_cache = Nlp(csv_path="data/datafr_cleaned.csv")
    print("✅ Moteur NLP chargé avec succès!")
    return _nlp_engine_cache

def clean_nan_values(obj):
    """Remplace récursivement tous les NaN par None"""
    if isinstance(obj, dict):
        return {k: clean_nan_values(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [clean_nan_values(item) for item in obj]
    elif isinstance(obj, float):
        if math.isnan(obj) or math.isinf(obj):
            return None
        return obj
    return obj

@csrf_exempt
@api_view(['GET'])


def recommandations(request):
    user = request.user
    query = request.GET.get('query', '').strip()

    if query == "":
        return Response({"error": "Paramètre 'query' manquant."}, status=400)

    nlp_engine = get_nlp_engine()
    nlp_results = nlp_engine.Search_query(query, top_k=5)
    
    if user and user.is_authenticated:
        try:
            final_results = filter_by_content(user, nlp_results)
        except AttributeError:
            final_results = nlp_results
    else:
        final_results = nlp_results

    # ✅ NETTOYER TOUS LES NaN AVANT DE RETOURNER
    final_results = clean_nan_values(final_results)

    return Response({
        "query": query,
        "count": len(final_results),
        "results": final_results,
    })
@csrf_exempt
@api_view(['POST'])
def reload_dataset(request):
    """Force le rechargement du dataset"""
    global _nlp_engine_cache
    
    old_cache_exists = _nlp_engine_cache is not None
    _nlp_engine_cache = None
    
    # Recharger immédiatement
    nlp_engine = get_nlp_engine()
    
    return Response({
        "message": "Dataset rechargé avec succès!",
        "was_cached": old_cache_exists,
        "csv_path": "data/datafr_cleaned.csv"
    })

print("🟢 api/views.py complètement chargé!")