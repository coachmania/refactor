from django.urls import path
from .views import Content, Customize

urlpatterns = [
	path('content/', Content.as_view(), name='content'),
	path('customize/', Customize.as_view(), name='customize'),
]