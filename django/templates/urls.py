from django.urls import path
from .views import Scheme

urlpatterns = [
    path('scheme/<int:id>/', Scheme.as_view(), name='scheme'),
]