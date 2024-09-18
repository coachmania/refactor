from django.urls import path
from .views import Item, Items
from core.views import Add, Delete, FieldsMultiple
from .models import Lang

urlpatterns = [
    path('add/', Add.as_view(model=Lang), name='add'),
    path('delete/<int:id>/', Delete.as_view(model=Lang), name='delete'),
    path('fields/<int:id>/', FieldsMultiple.as_view(model=Lang), name='fields'),
    path('item/<int:id>/', Item.as_view(), name='item'),
    path('items/', Items.as_view(), name='items'),
]