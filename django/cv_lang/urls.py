from django.urls import path
from .views import Item, Items, Fields

urlpatterns = [
    path('item/<int:lang_id>/', Item.as_view(), name='item'),
    path('items/', Items.as_view(), name='items'),
    path('fields/<int:id>/', Fields.as_view(), name='fields'),
]