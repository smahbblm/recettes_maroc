from django.contrib import admin
from django.apps import apps


# Dynamically register all models in the 'recettes' app so they appear in
# the Django admin even when models are split across multiple files.
try:
	app_models = apps.get_app_config('preferences').get_models()
	for model in app_models:
		try:
			admin.site.register(model)
		except admin.sites.AlreadyRegistered:
			pass
except LookupError:
	# If the app config is not yet ready (e.g. during some management
	# commands or early import time), skip dynamic registration. The admin
	# will still work when Django starts normally after migrations.
	pass
