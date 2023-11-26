from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, ProductDetailViewSet

router = DefaultRouter()
router.register(r'^list', ProductViewSet, basename='products')
router.register(r'^list/<int:pk>', ProductDetailViewSet, basename='products')

urlpatterns = router.urls