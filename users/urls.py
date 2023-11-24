from rest_framework.routers import DefaultRouter

from .views import UserDetailViewSet, UserViewSet

router = DefaultRouter()
router.register(r'^list', UserViewSet, basename='users')
router.register(r'^list/<str:pk>', UserDetailViewSet, basename='users')

urlpatterns = router.urls
