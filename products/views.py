from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from .models import Product
from .serializers import GeneralProductSerializer, DetailProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.AllowAny]

    queryset = Product.objects.all().order_by('created_at')
    serializer_class = GeneralProductSerializer

class ProductDetailViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.AllowAny]
    
    queryset = Product.objects.all()
    serializer_class = DetailProductSerializer
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print(serializer.data)
        return Response(serializer.data)


# from rest_framework import viewsets
# from rest_framework import permissions

# from .models import Product
# from .serializers import ProductSerializer

# class ProductViewSet(viewsets.ModelViewSet):
#     permission_classes=[permissions.AllowAny]

#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductDetailViewSet(viewsets.ModelViewSet):
#     permission_classes=[permissions.AllowAny]
    
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
