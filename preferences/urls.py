from django.urls import path
from . import views

urlpatterns = [
    path('api/categories/', views.CategorieListView.as_view()),
    path('api/regions/', views.RegionListView.as_view()),
    path('api/ingredients/', views.IngredientListView.as_view()),
    path('api/preferences/', views.PreferenceView.as_view()),
]
