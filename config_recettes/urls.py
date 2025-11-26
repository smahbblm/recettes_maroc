# config_recettes/urls.py
from django.contrib import admin
from django.urls import path, include

from recettes.views import CategorieListView, RegionListView, IngredientListView

urlpatterns = [
    # vos URLs existantes
    path('api/categories/', CategorieListView.as_view()),
    path('api/regions/', RegionListView.as_view()),
    path('api/ingredients/', IngredientListView.as_view()),
]
