from apps.api.serializers import ProductSerializer, CustomerSerializer, TicketSerializer
from apps.products.models import Product
from apps.customers.models import Customer
from apps.consumers.models import Ticket
from rest_framework import viewsets
from rest_framework import permissions


class ProductPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user and request.user.is_authenticated


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (ProductPermission, )
    lookup_field = 'id'
    
    
    
class CustomerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user and request.user.is_authenticated


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = (CustomerPermission, )
    lookup_field = 'id'
    
    
     
class TicketPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user and request.user.is_authenticated


class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Ticket.objects.all()
    permission_classes = (CustomerPermission, )
    lookup_field = 'id'
    
    
    