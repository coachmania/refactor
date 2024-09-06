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

class TokenRefresh(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        return Response({'error': 'Token refresh is disabled'}, status=status.HTTP_200_OK)
        refresh_token = request.COOKIES.get('refresh_token')
        if refresh_token is None:
            return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)
        print(refresh_token)

        # try:
        #     refresh = RefreshToken(refresh_token)
        #     access_token = str(refresh.access_token)

        #     response = Response({
        #         'message': 'Token refreshed successfully',
        #     })

        #     response.set_cookie(
        #         'access_token', 
        #         access_token, 
        #         httponly=True, 
        #         # TODO ici mettre secure=True pour la production
        #         secure=False, 
        #         samesite='Lax'
        #     )

        #     return response
        # except Exception as e:
        #     return Response({'error': 'Invalid refresh token'}, status=status.HTTP_400_BAD_REQUEST)

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
                'access_token': access_token,
            })

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
        data = {
            'user': UserSerializer(user).data,
            'is_authenticated': user.is_authenticated
        }
        return Response(data, status=status.HTTP_200_OK)