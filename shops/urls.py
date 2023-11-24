from rest_framework import routers

from .views import ShopViewSet, ShopDetailViewSet

router = routers.DefaultRouter()
router.register(r'list', ShopViewSet, basename='shops')
router.register(r'list/<str:pk>/', ShopDetailViewSet, basename='shops')

urlpatterns = router.urls
