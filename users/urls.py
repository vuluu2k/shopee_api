from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'^list', views.UserViewSet, basename='users')
router.register(r'^banks', views.BankViewSet, basename='banks')

urlpatterns = router.urls
