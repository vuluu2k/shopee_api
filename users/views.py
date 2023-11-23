from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Profile
from .serializers import ProfileSerializer

@csrf_exempt
@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(data = serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status=status.HTTP_201_CREATED)
        return Response(data = serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PATCH'])
def user_detail(request, pk, test):
    if request.method == 'GET':
        profile = Profile.objects.get(pk = pk)
        serializer = ProfileSerializer(profile)
        return Response(data = serializer.data, status=status.HTTP_200_OK)

# in path call params (arg function)
# form post call body or form data (request.data)
# after ? call query (request.GET)