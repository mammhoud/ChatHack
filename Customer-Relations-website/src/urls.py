from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
#from chatapp.views import supporter_homepage

urlpatterns = [
    #path('accounts/', include('apps.accounts.urls')),
    #path('django-chatapp/chat/supporter/', supporter_homepage),
    #path('', include('chatapp.urls', namespace='chatapp')),

    path('cr/', include('apps.tickets.urls')),
    path("", include("apps.utils.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("apps.api.urls")),
    path("accounts/", include("apps.accounts.urls")),
    path("charts/", include("apps.charts.urls")),
    path("tables/", include("apps.tables.urls")),
    path("tasks/", include("apps.tasks.urls")),
    path('api/docs/schema', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path("__debug__/", include("debug_toolbar.urls")),
]

urlpatterns += static(settings.CELERY_LOGS_URL, document_root=settings.CELERY_LOGS_DIR)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
