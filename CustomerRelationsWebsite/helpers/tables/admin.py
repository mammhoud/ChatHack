from django.contrib import admin
from django.apps import apps

from import_export.admin import ImportExportModelAdmin


app_models = apps.get_app_config('tables').get_models()
for model in app_models:
    try:

        admin.site.register(model, ImportExportModelAdmin)

    except Exception:
        pass