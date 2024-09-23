"""
URL configuration for myproject project.

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
from django.urls import path

from myapp import views, category_views, product_views
from myapp import auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashborad/', views.dashboard, name='home'),

    #======================Authentication==============
    path('login/', auth_views.my_login, name='login'),
    path('logout/', auth_views.my_logout, name='logout'),

    # ======================Category==============

    path('category/create/', category_views.create_category, name='create_category'),
    path('category/index/', category_views.index_category, name='index_category'),

    path('category/edit/<int:id>/', category_views.edit_category, name='category_edit'),
    path('category/delete/<int:id>/', category_views.delete_category, name='category_delete'),
    path('category/update/<int:id>/', category_views.update_category, name='category_update'),

    # ======================Product==============

    path('product/create/', product_views.create_product, name='create_product'),
    path('product/index/', product_views.index_product, name='index_category'),



]
