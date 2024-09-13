from django.urls import path
from .views import Type, TitleDetails, Links, Fields

urlpatterns = [
    path('type/', Type.as_view(), name='type'),
    path('title/', TitleDetails.as_view(), name='title'),
    path('links/', Links.as_view(), name='links'),
    path('fields/', Fields.as_view(), name='fields'),
]