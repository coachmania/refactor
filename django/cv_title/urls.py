from django.urls import path
from .views import Fields

urlpatterns = [
    path('fields/', Fields.as_view(), name='fields'),
]