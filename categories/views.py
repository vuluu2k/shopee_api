from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Category
from .serializers import CategorySerializer
from products.models import Product
from products.serializers import DetailProductSerializer
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
            queryset = queryset.filter(
                Q(parent__id=category_id) | Q(id=category_id))
        return super().filter_queryset(queryset)


class ProductByCategoryViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    serializer_class = DetailProductSerializer
    queryset = Product.objects.all()

    def get_all_child_categories(self, category):
        children = Category.objects.filter(parent=category)
        for child in children:
            children = children | self.get_all_child_categories(child)
        return children

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter(
            'id', openapi.IN_QUERY, description="Category ID",
            type=openapi.TYPE_STRING
        ),
        openapi.Parameter(
            'shop', openapi.IN_QUERY, description="Shop",
            type=openapi.TYPE_STRING
        ),
        openapi.Parameter(
            'price_order', openapi.IN_QUERY, description="Price Order",
            type=openapi.TYPE_STRING
        ),
        openapi.Parameter(
            'sort_by', openapi.IN_QUERY, description="Sort By",
            type=openapi.TYPE_STRING
        ),

    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        category_id = self.request.query_params.get('id')
        params = {}
        if category_id:
            parent_category = Category.objects.get(id=category_id)
            all_child_categories = self.get_all_child_categories(
                parent_category)
            all_categories = all_child_categories | Category.objects.filter(
                id=parent_category.id)
            params['category__in'] = all_categories

        shop = self.request.query_params.get('shop')
        if shop:
            params['shop'] = shop

        # price_order = self.request.query_params.get('price_order')
        # queryset = queryset.order_by(price_order)

        # sort_by = self.request.query_params.get('sort_by')
        # if sort_by == 'newest':
        #     queryset = queryset.order_by('-created_at')

        # if sort_by == 'best_seller':
        #     one_month_ago = timezone.now() - timedelta(days=30)
        #     queryset = queryset.annotate(
        #         total_sold=Sum('variation__orderdetail__quantity',
        #                        filter=Q(variation__orderdetail__order__created_at__gte=one_month_ago,
        #                                 variation__orderdetail__order__status=2))
        #     ).order_by('-total_sold')

        queryset = queryset.filter(**params)

        return super().filter_queryset(queryset)
