from rest_framework import generics
from .models import Categorie, Region, Ingredient, PreferenceUtilisateur
from .serializers import CategorieSerializer, RegionSerializer, IngredientSerializer, PreferenceSerializer

class CategorieListView(generics.ListAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class RegionListView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class IngredientListView(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class PreferenceView(generics.CreateAPIView):
    serializer_class = PreferenceSerializer
