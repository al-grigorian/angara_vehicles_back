"""
URL configuration for angara_vehicles_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from angara_vehicles_app import views
from rest_framework import permissions

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.GetOptions, name='options_url'),
    path('option/<int:id>/', views.GetOption, name='option_url'),
    path('delete/<int:record_id>/', views.DeleteRecord, name='delete_record')
]