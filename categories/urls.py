from rest_framework.routers import DefaultRouter

from .views import CategoryViewset, ProductByCategoryViewset,MyApiView

router = DefaultRouter()
router.register(r'^list', CategoryViewset, basename='categories')
router.register(r'^viewproduct', ProductByCategoryViewset, basename='categories')
router.register(r'^myapi', MyApiView, basename='categories')

urlpatterns = router.urls