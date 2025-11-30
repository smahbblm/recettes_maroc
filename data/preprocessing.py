
"""
from unidecode import unidecode
import re
df=pd.read_csv("./datafr.csv")

print("Doublons exacts sur toutes les colonnes :", df.duplicated().sum())
print("Doublons sur le nom de la recette:",df.duplicated(subset=["name"]).sum())
duplicate_names=df[df.duplicated(subset=["name"],keep=False)]
print(duplicate_names)
df_clean=df.dropna(subset=["name","ingredients","instructions",])
print(df_clean.shape)
def clean_Text(text):
    if pd.isna(text):
        return ""
    text=text.lower()
    text=unidecode(text)
    text=re.sub(r'\s+',' ',text).strip()
    text = text.replace("'", "") 
    text = text.replace("*", "")

    return text
df_clean['name'] = df_clean['name'].apply(clean_Text)
df_clean['ingredients'] = df_clean['ingredients'].apply(clean_Text)
df_clean['instructions'] = df_clean['instructions'].apply(clean_Text)


df_clean.to_csv("./datafr_cleaned.csv", index=False)

df[df["image_url"].isna()]
default_imageurl="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGaf_p8WUMQu664cib9kpdFSmHiOlIfltjLozlKoyUYM1DUS9QNrXRdIS9qL2nElCoEeg&usqp=CAU"
df["image_url"]=df["image_url"].fillna(default_imageurl)

print("nbr",df[df["image_url"].isna()].shape[0])

"""
import pandas as pd

file_path = "./datafr_cleaned.csv"

# 1. Charger les données
df = pd.read_csv(file_path)

print(f"📊 Nombre total de lignes : {len(df)}")

# 2. Définir les URLs
url_non_dispo_ancienne = "https://www.la-cuisine-marocaine.com/photos-recettes/non-disponible.jpg"
url_non_dispo_nouvelle = "https://alimentsain.fr/wp-content/uploads/2025/03/10-recettes-marocaines-pour-se-regaler-de-lentree-au-dessert-pendant-le-Ramadan.jpg"
default_imageurl = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGaf_p8WUMQu664cib9kpdFSmHiOlIfltjLozlKoyUYM1DUS9qNrXRdIS9qL2nElCoEeg&usqp=CAU"

# 3. Vérifier les images invalides AVANT modification
print(f"\n🔍 Images 'non-disponible.jpg' avant modification : {(df['image_url'] == url_non_dispo_ancienne).sum()}")
print(f"🔍 Images vides ou NaN avant modification : {(df['image_url'].isna() | (df['image_url'] == '')).sum()}")

# 4. Appliquer les modifications dans le bon ordre
# D'abord remplacer l'ancienne URL "non-disponible"
df["image_url"] = df["image_url"].replace(url_non_dispo_ancienne, url_non_dispo_nouvelle)

# Ensuite remplacer les valeurs vides par l'image par défaut
df["image_url"] = df["image_url"].fillna(default_imageurl)
df["image_url"] = df["image_url"].replace("", default_imageurl)

# 5. Vérifier les modifications APRÈS
print(f"\n✅ Images 'non-disponible.jpg' après modification : {(df['image_url'] == url_non_dispo_ancienne).sum()}")
print(f"✅ Images avec nouvelle URL : {(df['image_url'] == url_non_dispo_nouvelle).sum()}")
print(f"✅ Images vides ou NaN après modification : {(df['image_url'].isna() | (df['image_url'] == '')).sum()}")

# 6. Afficher quelques exemples
print("\n📷 Aperçu des 10 premières images :")
print(df["image_url"].head(10))

# 7. Sauvegarder le fichier
df.to_csv(file_path, index=False)
print(f"\n💾 Fichier sauvegardé : {file_path}")
