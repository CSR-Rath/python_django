from django.urls import path, include

from apiApp import views_category

from .views_category import (
    home,
    get_categories,
    get_category,
    post_category,
    put_category,
    delete_category,
)

urlpatterns = [
    path('', home, name='home'),
    # ========================== For Category ======================================
    path('api/categories/', get_categories, name='get_categories'),  # GET all categories
    path('api/categories/post/', post_category, name='post_category'),  # POST a new category
    path('api/categories/filter/<int:category_id>/', get_category, name='get_category'),  # GET a single category
    path('api/categories/put/<int:category_id>/', put_category, name='put_category'),  # PUT update category
    path('api/categories/delete/<int:category_id>/', delete_category, name='delete_category'),  # DELETE category

]
