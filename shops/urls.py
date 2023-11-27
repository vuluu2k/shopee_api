from rest_framework import routers

from .views import ShopViewSet

router = routers.DefaultRouter()
router.register(r'list', ShopViewSet, basename='shops')

urlpatterns = router.urls
