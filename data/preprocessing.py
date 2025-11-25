import pandas as pd
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
