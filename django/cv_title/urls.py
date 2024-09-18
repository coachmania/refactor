from django.urls import path
from .views import Type, TitleDetails, Links
from core.views import Update
from .models import Title

urlpatterns = [
    path('update/', Update.as_view(model=Title), name='update'),
    path('type/', Type.as_view(), name='type'),
    path('title/', TitleDetails.as_view(), name='title'),
    path('links/', Links.as_view(), name='links'),
]