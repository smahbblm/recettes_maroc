# configuration des routes API (ex: /api/recommandations/)()
from django.urls import path
from .views import recommandations,reload_dataset

urlpatterns = [
    path('recommandations/', recommandations, name='recommandations'),
    path('reload-dataset/', reload_dataset, name='reload_dataset'),
]

