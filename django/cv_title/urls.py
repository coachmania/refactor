from django.urls import path
from .views import Update, Type

urlpatterns = [
    path('update/', Update.as_view(), name='update'),
    path('type/', Type.as_view(), name='type'),
]