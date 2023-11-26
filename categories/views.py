from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import permissions

from .models import Category
from .serializers import CategorySerializer
# from products.models import Product
# from products.serializers import GeneralProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.AllowAny]

    queryset = Category.objects.all().order_by('created_at')
    serializer_class = CategorySerializer

class CategoryDetailViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.AllowAny]
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# def get_all_child_categories(category):
#     children = Category.objects.filter(parent=category)
#     if children:
#         for child in children:
#             children = children.union(get_all_child_categories(child))
#     return children

# class ProductByCategoryViewSet(viewsets.ModelViewSet):
#     permission_classes=[permissions.AllowAny]
    
#     serializer_class = GeneralProductSerializer

#     def get_queryset(self):
#         queryset = Product.objects.all()
#         category_id = self.request.query_params.get('category_id', None)
#         if category_id is not None:
#             category = Category.objects.get(id=category_id)
#             child_categories = get_all_child_categories(category)
#             queryset = queryset.filter(category_id__in=child_categories)
#         return queryset