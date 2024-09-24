from django.urls import path
from .views import Fields, Scheme, SettingsListCreateView, SettingsDetailView
from core.views import Update
from .models import Settings

urlpatterns = [
	path('update/', Update.as_view(model=Settings), name='update'),
	path('fields/', Fields.as_view(), name='fields'),
	path('scheme/<int:id>/', Scheme.as_view(), name='scheme'),
	path('settings/', SettingsListCreateView.as_view(), name='settings_list'),
    path('settings/<int:pk>/', SettingsDetailView.as_view(), name='settings_detail'),

]