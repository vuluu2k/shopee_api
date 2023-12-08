from rest_framework import permissions
from rest_framework import viewsets

from .models import User, BankCard
from .serializers import UserSerializer, BankSerializer

class BankViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    queryset = BankCard.objects.all()
    serializer_class = BankSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer



    