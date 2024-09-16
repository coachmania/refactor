from django.urls import path
from .views import Items, Fields

urlpatterns = [
    path('items/', Items.as_view(), name='items'),
    path('fields/<int:id>/', Fields.as_view(), name='fields'),
]