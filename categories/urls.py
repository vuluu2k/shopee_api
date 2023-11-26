from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, CategoryDetailViewSet

router = DefaultRouter()
router.register(r'^list', CategoryViewSet, basename='categories')
router.register(r'^list/<int:pk>', CategoryDetailViewSet, basename='categories')
# router.register(r'^list/products/', ProductByCategoryViewSet, basename='categories')

urlpatterns = router.urls