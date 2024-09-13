from django.urls import path
from .views import Fields

urlpatterns = [
    path('fields/<int:id>/', Fields.as_view(), name='fields'),
]