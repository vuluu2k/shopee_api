from rest_framework import permissions
from rest_framework import viewsets

from .models import User, BankCard
from .serializers import UserSerializer, BankSerializer
from shopee_clone.permissions import IsOwnerOrReadOnly, IsSuperUser


class BankViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    queryset = BankCard.objects.all()
    serializer_class = BankSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer

    def get_permissions(self):
        if(self.action == 'create'):
            return [permissions.AllowAny()]
        if(self.action == 'list'):
            return [IsSuperUser()]
        else:
            return [IsOwnerOrReadOnly()]



    