from django.urls import path
from .views import Fields, Scheme
from core.views import Update
from .models import Settings

urlpatterns = [
	path('update/', Update.as_view(model=Settings), name='update'),
	path('fields/', Fields.as_view(), name='fields'),
	path('scheme/<int:id>/', Scheme.as_view(), name='scheme'),
]