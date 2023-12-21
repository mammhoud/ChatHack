from django.contrib import admin
# from .models import Ticket, Comment
from django.apps import apps
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin

app_models = apps.get_app_config('products').get_models()
for model in app_models:
    try:
        admin.site.register(model, ImportExportModelAdmin)

    except Exception:
        print("Not registered, %s" % model.__name__, User.__name__)
