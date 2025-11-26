from sentence_transformers import SentenceTransformer
import pandas as pd 
import faiss
import numpy as np
from numpy.linalg import norm
class Nlp:
    def __init__(self,csv_path="./datafr_cleaned.csv"):
        
        self.df=pd.read_csv(csv_path)
        self.df["full_text"]=(
        self.df["name"].fillna("")+" ."+
        self.df["ingredients"].fillna("")+" . "+
        self.df["instructions"].fillna(""))
        texts=self.df["full_text"].tolist()
        self.model=SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings=self.model.encode(texts,batch_size=64,show_progress_bar=True,convert_to_numpy=True)
        d=self.embeddings.shape[1]
        self.index=faiss.IndexFlatL2(d)
        self.index.add(self.embeddings)
    
    def Search_query(self,query,top_k=10):
        resultats=[]
        vector_query = self.model.encode([query], convert_to_numpy=True)[0]
        D,I=self.index.search(np.array([vector_query],dtype='float32'),top_k)
        for idx in I[0]:
            row=self.df.iloc[idx]
            resultats.append({
                 "name": row["name"],
                "ingredients": row["ingredients"],
                "instructions": row["instructions"],
                "preparation_time": row.get("preparation_time", None),
                "cooking_time": row.get("cooking_time", None),
                "total_time": row.get("total_time", None),
                "image_url": row.get("image_url", None),
                "source": row.get("source", None)


            })
        return resultats
       


   




