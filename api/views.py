#  Les Vues API (reçoit la requête et appelle le moteur).

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .services.recommender_engine import filter_by_content
from .services.nlp_engine import Nlp

nlp_engine = Nlp(csv_path="data/datafr_cleaned.csv")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommandations(request):
    user = request.user
    query = request.GET.get('query', '').strip()

    if query == "":
        return Response({"error": "Paramètre 'query' manquant."}, status=400)

    nlp_results = nlp_engine.Search_query(query, top_k=20)
    final_results = filter_by_content(user, nlp_results)

    return Response({
        "query": query,
        "count": len(final_results),
        "results": final_results,
    })
