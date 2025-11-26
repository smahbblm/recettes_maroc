from django.urls import path
from . import views

urlpatterns = [
    path('api/categories/', views.categorie_list),
    path('api/regions/', views.region_list),
    path('api/ingredients/', views.ingredient_list),
]
