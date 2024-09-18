from django.urls import path
from .views import Add, Item, Items
from core.views import FieldsMultiple
from .models import Lang

urlpatterns = [
    path('add/', Add.as_view(), name='add'),
    path('item/<int:id>/', Item.as_view(), name='item'),
    path('delete/<int:id>/', Item.as_view(), name='delete'),
    path('items/', Items.as_view(), name='items'),
    path('fields/<int:id>/', FieldsMultiple.as_view(model=Lang), name='fields'),
]