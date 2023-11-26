from rest_framework import viewsets, generics, mixins
from rest_framework import permissions
from rest_framework.response import Response

from .models import Product
from .serializers import GeneralProductSerializer, DetailProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.AllowAny]

    queryset = Product.objects.all().order_by('created_at')
    serializer_class = GeneralProductSerializer
    lookup_field = 'slug'
    def get_serializer_class(self):
        if self.action == 'list':
            return GeneralProductSerializer
        elif self.action == 'retrieve' or self.action == 'create':
            return DetailProductSerializer
        return GeneralProductSerializer