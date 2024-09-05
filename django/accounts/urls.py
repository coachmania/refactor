from django.urls import path
from .views import TokenObtain, Login, Logout, Profile

urlpatterns = [
    path('token/obtain/', TokenObtain.as_view(), name='token_obtain'),

    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', Profile.as_view(), name='profile'),
]