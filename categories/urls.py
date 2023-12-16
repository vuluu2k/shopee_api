from django.urls import path

from .views import CategoryViewset, ProductByCategoryViewset

urlpatterns = [
    path('', CategoryViewset.as_view({'get': 'list', 'post': 'create'})),
    path('/<str:pk>', CategoryViewset.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
    path('/product', ProductByCategoryViewset.as_view({'get': 'list'})),
    
]