from django.urls import path
from .views import Add, Item, Items, Fields

urlpatterns = [
    path('add/', Add.as_view(), name='add'),
    path('item/<int:id>/', Item.as_view(), name='item'),
    path('delete/<int:id>/', Item.as_view(), name='delete'),
    path('items/', Items.as_view(), name='items'),
    path('fields/<int:id>/', Fields.as_view(), name='fields'),
]