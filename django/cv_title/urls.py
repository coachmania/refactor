from django.urls import path
from .views import Type, Fields

urlpatterns = [
    path('type/', Type.as_view(), name='type'),
    path('fields/', Fields.as_view(), name='fields'),
]