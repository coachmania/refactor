from django.urls import path
from .views import Type

urlpatterns = [
    path('type/', Type.as_view(), name='type'),
]