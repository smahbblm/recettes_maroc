# test_nlp.py
from nlp_engine import Nlp

# Initialiser le modèle avec ton CSV
nlp = Nlp(csv_path="../../data/datafr_cleaned.csv")


# Poser une question
query = "couscous au poulet"
resultats = nlp.Search_query(query, top_k=5)

# Afficher les résultatscd
for i, r in enumerate(resultats, 1):
    print(f"--- Résultat {i} ---")
    print("Nom:", r["name"])
    print("Ingrédients:", r["ingredients"])
    print("Instructions:", r["instructions"])
    print("Temps de préparation:", r["preparation_time"])
    print("Temps de cuisson:", r["cooking_time"])
    print("Temps total:", r["total_time"])
    print("Image:", r["image_url"])
    print("Source:", r["source"])
    print("\n")
