from django.urls import path
from .views import Type, Details, Field

urlpatterns = [
    path('type/', Type.as_view(), name='type'),
    path('details/', Details.as_view(), name='details'),
    path('field/', Field.as_view(), name='field'),
]