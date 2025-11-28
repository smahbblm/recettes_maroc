# views.py

import json # <-- NOUVEL IMPORT NÉCESSAIRE POUR LIRE LE JSON POSTÉ
from django.http import JsonResponse
from django.contrib.auth.models import User
from recettes.models import Categorie, Region, Ingredient 
from preferences.models import PreferenceUtilisateur # <-- NOUVEL IMPORT CRUCIAL

def categorie_list(request):
    categories = list(Categorie.objects.values('id', 'nom'))
    return JsonResponse({'categories': categories})

def region_list(request):
    regions = list(Region.objects.values('id', 'nom'))
    return JsonResponse({'regions': regions})

def ingredient_list(request):
    ingredients = list(Ingredient.objects.values('id', 'nom'))
    return JsonResponse({'ingredients': ingredients})

# ... Les fonctions categorie_list, region_list, ingredient_list sont au-dessus...

def preference_create(request):
    if request.method == 'POST':
        try:
            # 1. Obtenir l'utilisateur
            user = User.objects.get(id=1)  
            
            # 2. Lire les données JSON envoyées par React
            data = json.loads(request.body)
            
            categories_ids = data.get('categories_preferees', [])
            regions_ids = data.get('regions_preferees', []) 
            ingredients_ids = data.get('ingredients_evites', [])

            
            # 3. Récupérer ou créer l'objet de préférence
            preference, created = PreferenceUtilisateur.objects.get_or_create(utilisateur=user)
            
            # A. Gérer les Catégories (M2M)
            categories_obj = Categorie.objects.filter(id__in=categories_ids)
            preference.categories_preferees.set(categories_obj) 

            # B. Gérer les Régions (M2M)
            regions_obj = Region.objects.filter(id__in=regions_ids)
            preference.regions_preferees.set(regions_obj) 
            
            # C. Gérer les Ingrédients (M2M)
            ingredients_obj = Ingredient.objects.filter(id__in=ingredients_ids)
            preference.ingredients_evites.set(ingredients_obj)

            return JsonResponse({'message': 'Préférences sauvegardées avec succès', 'status': 'ok', 'data_received': data}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Corps de requête JSON invalide'}, status=400)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde: {e}")
            return JsonResponse({'error': f"Erreur interne du serveur lors de la sauvegarde."}, status=500)
    
    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)
