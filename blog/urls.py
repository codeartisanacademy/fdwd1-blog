"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from blogapp.views import HomeView, DashboardView, SignUpView, CategoryAddView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')), # menginclude alamat2 utk authentication
    path('admin/', admin.site.urls),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', HomeView.as_view(), name="home"),
    path('dashboard/', DashboardView.as_view(), name='dashboard' ),
    path('category/add/', CategoryAddView.as_view(), name='category-add'),
]

# 127.0.0.1:8000/accounts/login
# 127.0.0.1:8000/accounts/logout