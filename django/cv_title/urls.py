from django.urls import path
from .views import Type, TitleDetails, Fields

urlpatterns = [
    path('type/', Type.as_view(), name='type'),
    path('title/', TitleDetails.as_view(), name='title'),
    path('fields/', Fields.as_view(), name='fields'),
]