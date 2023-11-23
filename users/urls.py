from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import user_list, user_detail

urlpatterns = [
    path('all/', user_list),
    path('detail/<str:pk>/<int:test>/', user_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)