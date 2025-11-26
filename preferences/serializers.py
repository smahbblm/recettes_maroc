from rest_framework import serializers
from .models import PreferenceUtilisateur
from recettes.models import Categorie, Region, Ingredient

class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreferenceUtilisateur
        fields = ['categories_preferees', 'regions_preferees', 'ingredients_evites']
    
    def create(self, validated_data):
        # Récupérer l'utilisateur connecté
        user = self.context['request'].user
        
        # Créer ou récupérer les préférences
        preference, created = PreferenceUtilisateur.objects.get_or_create(
            utilisateur=user,
            defaults={}
        )
        
        # Mettre à jour les relations ManyToMany
        if 'categories_preferees' in validated_data:
            preference.categories_preferees.set(validated_data['categories_preferees'])
        
        if 'regions_preferees' in validated_data:
            preference.regions_preferees.set(validated_data['regions_preferees'])
            
        if 'ingredients_evites' in validated_data:
            preference.ingredients_evites.set(validated_data['ingredients_evites'])
        
        return preference

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
