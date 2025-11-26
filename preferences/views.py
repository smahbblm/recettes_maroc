from django.http import JsonResponse
from recettes.models import Categorie, Region, Ingredient

def categorie_list(request):
    categories = list(Categorie.objects.values('id', 'nom'))
    return JsonResponse({'categories': categories})

def region_list(request):
    regions = list(Region.objects.values('id', 'nom'))
    return JsonResponse({'regions': regions})

def ingredient_list(request):
    ingredients = list(Ingredient.objects.values('id', 'nom'))
    return JsonResponse({'ingredients': ingredients})
