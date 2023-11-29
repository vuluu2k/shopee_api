from rest_framework import viewsets
from rest_framework import permissions

from .models import Category
from .serializers import CategorySerializer
from products.models import Product
from products.serializers import GeneralProductSerializer
from django.db.models import Q


class CategoryViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def filter_queryset(self, queryset):
        category_id = self.request.query_params.get('id')
        if category_id:
            queryset = queryset.filter(Q(parent__id=category_id) | Q(id=category_id))
        return super().filter_queryset(queryset)
    
class ProductByCategoryViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    serializer_class = GeneralProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category_id = self.request.query_params.get('id')
        if category_id:
            queryset = queryset.filter(Q(category__parent__id=category_id) | Q(category__id=category_id))
        return super().filter_queryset(queryset)