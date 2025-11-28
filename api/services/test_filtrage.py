import os
import django

# Initialise Django correctement
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config_recettes.settings')
django.setup()

from django.contrib.auth import get_user_model
from api.services.recommender_engine import filter_by_content
from api.services.nlp_engine import Nlp

def test_filtrage(user_id, query):
    User = get_user_model()
    user = User.objects.get(id=user_id)
    csv_path = os.path.join(os.path.dirname(__file__), "../../data/datafr_cleaned.csv")
    nlp = Nlp(csv_path)
    nlp_results = nlp.Search_query(query, top_k=10)
    resultats = filter_by_content(user, nlp_results)

    print(f"Résultats personnalisés pour '{query}' et user {user_id}:")
    for r in resultats:
        print(f"Nom: {r['name']} | Score: {r['score_content']}")
        print(f"Ingrédients: {r['ingredients']}")
        print("-" * 40)

if __name__ == "__main__":
    test_filtrage(user_id=1, query="couscous au poulet")
