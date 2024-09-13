from django.urls import path
from .views import Infos, Fields

urlpatterns = [
    path('infos/', Infos.as_view(), name='infos'),
    path('fields/', Fields.as_view(), name='fields'),
]