"""
URL configuration for Publication project.

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
from home.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('explore/', explore_page, name='explore'),
    path('careers/', career_page, name='careers'),
    path('pricing/', pricing_page, name='pricing'),
    path('about/', about_page, name='about'),
    path('buyplan/', form_page, name='buyplan'),
    path('buyisbn/', cover_form_page, name='buyisbn'),
    path('buyedit/', edit_form_page, name='buyedit'),
    path('login/', login_page, name = 'login'),
    path('register/', register_page, name = 'register'),
    path('logout_page/', logout_page, name = 'logout_page'),
]
