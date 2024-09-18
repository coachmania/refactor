from django.urls import path
from .views import Item, Items
from core.views import Add, Delete, UpdateWithId
from .models import Lang

urlpatterns = [
    path('add/', Add.as_view(model=Lang), name='add'),
    path('delete/<int:id>/', Delete.as_view(model=Lang), name='delete'),
    path('update/<int:id>/', UpdateWithId.as_view(model=Lang), name='update'),
    path('item/<int:id>/', Item.as_view(), name='item'),
    path('items/', Items.as_view(), name='items'),
]