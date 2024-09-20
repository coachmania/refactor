from django.urls import path
from .views import Content

urlpatterns = [
	path('content/', Content.as_view(), name='content'),
]