from rest_framework import permissions
from rest_framework import viewsets

from .models import Shop
from .serializers import ShopSerializer

class ShopViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.AllowAny]

    queryset = Shop.objects.all().order_by('-created_at')
    serializer_class = ShopSerializer

class ShopDetailViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.AllowAny]

    queryset = Shop.objects.all()
    serializer_class = ShopSerializer