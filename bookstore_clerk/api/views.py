from django.shortcuts import render
from .models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, View
from .serializers import UserLoginSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response({"message":"Incorrect password"}, status=status.HTTP_400_BAD_REQUEST) 
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)