from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'^list', views.UserViewSet, basename='users')
router.register(r'^list/<str:pk>', views.UserDetailViewSet, basename='users')
router.register(r'^banks', views.BankViewSet, basename='banks')
router.register(r'^banks/<str:pk>', views.BankDetailViewSet, basename='banks')

urlpatterns = router.urls
