from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import UserSerializer

@method_decorator(csrf_exempt, name='dispatch')
class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            response = Response({
                'message': 'Logged in successfully',
            })

            response['Authorization'] = f'Bearer {access_token}'
            response.set_cookie(
                'refresh_token', 
                refresh_token, 
                httponly=True, 
                # TODO ici mettre secure=True pour la production
                secure=False, 
                samesite='Lax'
            )

            return response
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@method_decorator(csrf_exempt, name='dispatch')
class Logout(APIView):
    def post(self, request):
        logout(request)

        response = Response({
            'message': 'Logged out successfully',
        })

        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')

        return response

@method_decorator(csrf_exempt, name='dispatch')
class Profile(APIView):
    def get(self, request):
        user = request.user
        return JsonResponse({
            'user': UserSerializer(user).data,
            'message': 'User is authenticated'
        })