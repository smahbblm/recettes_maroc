import os
import sys

# Ajouter la racine du projet (recettes_maroc) au PYTHONPATH
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)

# Définir le settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config_recettes.settings')

import django
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

    for recette in resultats:

      print("Nom:", recette.get("nom"))
      print("Score:", recette.get("score_content"))
      print("Ingrédients:", recette.get("ingredients"))
      print("Instructions:", recette.get("instructions"))
      print("Image:", recette.get("image_url"))
      print("Préparation:", recette.get("preparation_time"))
      print("Cuisson time:", recette.get("cooking_time"))
      print("Total time:", recette.get("total_time"))
      print("Source:", recette.get("source"))
      print("---------------------------------------")


if __name__ == "__main__":
    test_filtrage(user_id=1, query="couscous au poulet")
