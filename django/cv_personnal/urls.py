from django.urls import path
from .views import Picture, Infos, Address, Mobility, Fields

urlpatterns = [
    path('picture/', Picture.as_view(), name='picture'),
    path('infos/', Infos.as_view(), name='infos'),
    path('address/', Address.as_view(), name='address'),
    path('mobility/', Mobility.as_view(), name='mobility'),
    path('fields/', Fields.as_view(), name='fields'),
]