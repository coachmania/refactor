from django.urls import path
from .models import Experience
from .views import Add, Item, Items
from core.views import FieldsMultiple

urlpatterns = [
    path('add/', Add.as_view(), name='add'),
    path('item/<int:id>/', Item.as_view(), name='item'),
    path('delete/<int:id>/', Item.as_view(), name='delete'),
    path('items/', Items.as_view(), name='items'),
    path('fields/<int:id>/', FieldsMultiple.as_view(model=Experience), name='fields'),
]