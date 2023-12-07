from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

router = DefaultRouter()
router.register(r'^list', views.UserViewSet, basename='users')
router.register(r'^banks', views.BankViewSet, basename='banks')
router.register(r'^jwt', views.MyApiView, basename='jwt-authentication')

urlpatterns = router.urls
