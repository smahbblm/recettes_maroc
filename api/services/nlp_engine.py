from sentence_transformers import SentenceTransformer
import pandas as pd 
import faiss
import numpy as np
import pickle
import os

class Nlp:
    def __init__(self, csv_path="./datafr_cleaned.csv", cache_path="./embeddings_cache.pkl"):
        
        # Vérifier si le cache existe
        if os.path.exists(cache_path):
            print("📂 Chargement depuis le cache...")
            with open(cache_path, 'rb') as f:
                cache = pickle.load(f)
                self.df = cache['df']
                self.embeddings = cache['embeddings']
                self.index = cache['index']
            
            # Charger uniquement le modèle (léger)
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
            print("✅ Cache chargé en quelques secondes!")
        
        else:
            print("🔄 Première initialisation - Calcul des embeddings (cela prendra ~20 minutes)...")
            
            # Charger et préparer les données
            self.df = pd.read_csv(csv_path)
            self.df["full_text"] = (
                self.df["name"].fillna("") + " ." +
                self.df["ingredients"].fillna("") + " . " +
                self.df["instructions"].fillna("")
            )
            texts = self.df["full_text"].tolist()
            
            # Charger le modèle et calculer les embeddings
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
            self.embeddings = self.model.encode(
                texts, 
                batch_size=64, 
                show_progress_bar=True, 
                convert_to_numpy=True
            )
            
            # Créer l'index FAISS
            d = self.embeddings.shape[1]
            self.index = faiss.IndexFlatL2(d)
            self.index.add(self.embeddings)
            
            # Sauvegarder dans le cache
            print("💾 Sauvegarde du cache...")
            with open(cache_path, 'wb') as f:
                pickle.dump({
                    'df': self.df,
                    'embeddings': self.embeddings,
                    'index': self.index
                }, f)
            print("✅ Cache créé avec succès!")
    
def Search_query(self, query, top_k=5, threshold=1.1):
    resultats = []

    vector_query = self.model.encode([query], convert_to_numpy=True)[0]

    D, I = self.index.search(
        np.array([vector_query], dtype="float32"),
        top_k
    )

    print("Distances FAISS:", D[0])  # ✅ debug

    for distance, idx in zip(D[0], I[0]):

        # ✅ ON SUPPRIME LES PLATS NON LIÉS
        if distance > threshold:
            continue

        row = self.df.iloc[idx]

        def safe_value(val):
            return None if pd.isna(val) else val

        resultats.append({
            "name": safe_value(row["name"]),
            "ingredients": safe_value(row["ingredients"]),
            "instructions": safe_value(row["instructions"]),
            "image_url": safe_value(row.get("image_url")),
            "score": float(distance)
        })

    return resultats   # ✅ peut contenir 0, 1, 2, 3... résultats SEULEMENT
