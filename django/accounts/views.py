from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from django.http import JsonResponse

class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            response = JsonResponse({
                'user': UserSerializer(user).data
            })

            response.set_cookie(
                'access_token', 
                access_token, 
                httponly=True, 
                secure=True,
                samesite='Lax'
            )
            response.set_cookie(
                'refresh_token', 
                str(refresh), 
                httponly=True, 
                secure=True, 
                samesite='Lax'
            )
            return response
        
        return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class Profile(APIView):
    def get(self, request):
        user = request.user
        return JsonResponse({
            'user': UserSerializer(user).data,
            'message': 'User issss'
        })