from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer
from products.models import Product
from products.serializers import GeneralProductSerializer
from django.db.models import Q
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta


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
    queryset = Product.objects.all()

    def get_all_child_categories(self, category):
        children = Category.objects.filter(parent=category)
        for child in children:
            children = children | self.get_all_child_categories(child)
        return children

    def filter_queryset(self, queryset):
        category_id = self.request.query_params.get('id')
        if category_id:
            parent_category = Category.objects.get(id=category_id)
            all_child_categories = self.get_all_child_categories(parent_category)
            all_categories = all_child_categories | Category.objects.filter(id=parent_category.id)
            queryset = queryset.filter(category__in=all_categories)

        shop = self.request.query_params.get('shop')
        if shop:
            queryset = queryset.filter(shop=shop)

        price_order = self.request.query_params.get('price_order')
        if price_order == 'asc':
            queryset = queryset.order_by('price')
        elif price_order == 'desc':
            queryset = queryset.order_by('-price')

        sort_by = self.request.query_params.get('sort_by')
        if sort_by == 'newest':
            queryset = queryset.order_by('-created_at')
        
        if sort_by == 'best_seller':
            one_month_ago = timezone.now() - timedelta(days=30)
            queryset = queryset.annotate(
            total_sold=Sum('variation__orderdetail__quantity', 
                           filter=Q(variation__orderdetail__order__created_at__gte=one_month_ago,
                                    variation__orderdetail__order__status=2))
        ).order_by('-total_sold')
        

        return super().filter_queryset(queryset)