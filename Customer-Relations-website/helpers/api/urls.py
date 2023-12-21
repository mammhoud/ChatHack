from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.api.views import ProductViewSet, TicketViewSet

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'ticket', TicketViewSet, basename='ticket')

#app_name = 'apis'

urlpatterns = [
    path('', include(router.urls)),
]
