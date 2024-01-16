from django.urls import path, include

from .views import CategoryViewset, ProductByCategoryViewset

urlpatterns = [
    path('', CategoryViewset.as_view({'get': 'list', 'post': 'create'})),
    path('/product',
         ProductByCategoryViewset.as_view({'get': 'list'})),
    path('/<str:pk>', include([
        path('', CategoryViewset.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        })),
    ])),
]
