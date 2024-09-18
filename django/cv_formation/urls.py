from django.urls import path
from .models import Formation
from .views import Item, Items
from core.views import Add, Delete, UpdateWithId

urlpatterns = [
    path('update/<int:id>/', UpdateWithId.as_view(model=Formation), name='update'),
    path('add/', Add.as_view(model=Formation), name='add'),
    path('delete/<int:id>/', Delete.as_view(model=Formation), name='delete'),
    path('item/<int:id>/', Item.as_view(), name='item'),
    path('items/', Items.as_view(), name='items'),
]