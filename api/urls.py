# configuration des routes API (ex: /api/recommandations/)()
from django.urls import path
from .views import recommandations

urlpatterns = [
    path('recommandations/', recommandations, name='recommandations'),
]


