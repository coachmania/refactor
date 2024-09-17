from django.urls import path
from .views import Add, Item, Items, Fields

urlpatterns = [
    path('add/', Add.as_view(), name='add'),
    path('item/<int:lang_id>/', Item.as_view(), name='item'),
    path('delete/<int:lang_id>/', Item.as_view(), name='delete'),
    path('items/', Items.as_view(), name='items'),
    path('fields/<int:lang_id>/', Fields.as_view(), name='fields'),
]