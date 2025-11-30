# config_recettes/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

# Appliquez le décorateur directement à la fonction
@ensure_csrf_cookie
def get_csrf(request):
    return JsonResponse({"detail": "CSRF cookie set"})

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('preferences.urls')),
    path('api/', include('api.urls')), 
    # Référencez la fonction get_csrf qui est déjà décorée
    path('api/csrf_token/', get_csrf, name='csrf_token'), 
]

