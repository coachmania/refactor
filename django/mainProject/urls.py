"""
URL configuration for mainProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('cv/', include('cv.urls')),
    path('cv_settings/', include('cv_settings.urls')),
    path('cv_title/', include('cv_title.urls')),
    path('cv_personnal/', include('cv_personnal.urls')),
    path('cv_lang/', include('cv_lang.urls')),
    path('cv_experience/', include('cv_experience.urls')),
    path('cv_formation/', include('cv_formation.urls')),
    path('cv_hobbie/', include('cv_hobbie.urls')),
]