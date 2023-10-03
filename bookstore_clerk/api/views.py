from django.shortcuts import render
from .models import User
from rest_framework.views import APIView, View
from .serializers import UserLoginSerializer
from rest_framework.response import Response
from rest_framework import status


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response({"message":"Incorrect password"}, status=status.HTTP_400_BAD_REQUEST) 