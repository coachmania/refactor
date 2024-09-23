from django.urls import path
from .views import Fields, Scheme

urlpatterns = [
    path('fields/', Fields.as_view(), name='fields'),
	path('scheme/<int:id>/', Scheme.as_view(), name='scheme'),
]