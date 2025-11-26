from rest_framework import serializers
from .models import Categorie, Region, Ingredient

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'nom']

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'nom']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'nom']
