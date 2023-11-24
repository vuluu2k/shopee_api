from rest_framework import permissions
from rest_framework import viewsets

from .models import Profile
from .serializers import ProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.AllowAny]

    queryset = Profile.objects.all().order_by('-created_at')
    serializer_class = ProfileSerializer
    
class UserDetailViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.AllowAny]

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer