from django.urls import path
from .models import Formation
from .views import Item, Items
from core.views import Add, Delete, FieldsMultiple

urlpatterns = [
    path('fields/<int:id>/', FieldsMultiple.as_view(model=Formation), name='fields'),
    path('add/', Add.as_view(model=Formation), name='add'),
    path('delete/<int:id>/', Delete.as_view(model=Formation), name='delete'),
    path('item/<int:id>/', Item.as_view(), name='item'),
    path('items/', Items.as_view(), name='items'),
]