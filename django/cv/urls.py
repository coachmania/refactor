from django.urls import path
from .views import Content

urlpatterns = [
	path('content/<int:id>/', Content.as_view(), name='content'),
]