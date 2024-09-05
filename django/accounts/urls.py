from django.urls import path
from .views import TokenObtain, Profile, Login, Logout, Profile
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/obtain/', TokenObtain.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', Profile.as_view(), name='profile'),

    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', Profile.as_view(), name='profile'),
]