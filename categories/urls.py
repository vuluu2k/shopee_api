from rest_framework.routers import DefaultRouter

from .views import CategoryViewset, ProductByCategoryViewset

router = DefaultRouter()
router.register(r'^list', CategoryViewset, basename='categories')
router.register(r'^viewproduct', ProductByCategoryViewset, basename='categories')

urlpatterns = router.urls