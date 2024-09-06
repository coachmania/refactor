from django.urls import path
from .views import TokenRefresh, Login, Profile, Logout
# from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/refresh/', TokenRefresh.as_view(), name='token_refresh'),
    path('login/', Login.as_view(), name='login'),
    path('profile/', Profile.as_view(), name='profile'),
    path('logout/', Logout.as_view(), name='logout'),
]