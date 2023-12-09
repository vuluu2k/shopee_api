from django.urls import path
from .views import UserViewSet, BankViewSet

urlpatterns = [
    path('', UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('/<str:pk>', UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
    path('/bank', BankViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('/bank/<str:pk>', BankViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
]
