from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import jwt
import json

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

class MyApiView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
    def get_queryset(self):
        token = self.request.query_params.get('access_token')
        try:
            decoded_data = jwt.decode(token, settings.ACCESS_TOKEN_SECRET, algorithms=['HS256'])
            return User.objects.filter(email=decoded_data["email"])
        except jwt.ExpiredSignatureError:
            refresh_token = self.request.query_params.get('refresh_token')
            try:
                decoded_data = jwt.decode(refresh_token, settings.REFRESH_TOKEN_SECRET, algorithms=['HS256'])
                new_token = jwt.encode({'email': decoded_data['email']}, settings.ACCESS_TOKEN_SECRET, algorithm='HS256')
                return User.objects.filter(email=decoded_data["email"])
            except jwt.InvalidTokenError:
                raise AuthenticationFailed('Invalid refresh token')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid access token')



    