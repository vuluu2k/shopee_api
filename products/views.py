from rest_framework import viewsets, generics, mixins
from rest_framework import permissions
from rest_framework.response import Response
from django.db.models import Q

from .models import Product
from .serializers import GeneralProductSerializer, DetailProductSerializer
from django_filters import rest_framework as filters


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name', 'category']


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    queryset = Product.objects.all().order_by('created_at')
    serializer_class = GeneralProductSerializer
    lookup_field = 'slug'

    filter_backends = filters.DjangoFilterBackend
    filterset_class = ProductFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return GeneralProductSerializer
        elif self.action == 'retrieve' or self.action == 'create':
            return DetailProductSerializer
        return GeneralProductSerializer

    # def filter_queryset(self, queryset):
    #     keyword = self.request.query_params.get('keyword')
    #     if keyword:
    #         queryset = queryset.filter(Q(name__icontains=keyword))
    #     return super().filter_queryset(queryset)
