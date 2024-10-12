# from importlib.resources import path
from django.urls import path

from .views_category import (
    startup,
    get_categories,
    post_category,
    get_category,
    put_category,
    delete_category,
)

from .views_product import (
    get_products,
    get_product,
    post_product,
    put_product,
    delete_product,
    filter_products
)


urlpatterns = [
    path('', startup, name='startup'),
    # ========================== For Category ======================================
    path('api/categories/', get_categories, name='get_categories'),  # GET all categories
    path('api/categories/post/', post_category, name='post_category'),  # POST a new category
    path('api/categories/put/<int:category_id>/', put_category, name='put_category'),  # PUT update category
    path('api/categories/delete/<int:category_id>/', delete_category, name='delete_category'),  # DELETE category
    path('api/categories/filter/<int:category_id>/', get_category, name='get_category'),  # GET a single category
    # ========================== For Category ======================================

    path('api/products/', get_products, name='get_products'),
    path('api/products/post/', post_product, name='post_product'),
    path('api/products/put/<int:product_id>/', put_product, name='put_product'),
    path('api/products/delete/<int:product_id>/', delete_product, name='delete_product'),
    path('api/products/get/<int:product_id>/', get_product, name='get_product'),
    path('api/products/filter/', filter_products, name='filter_products'),
# GET http://127.0.0.1:8000/api/products/filter/?id=1
# GET http://127.0.0.1:8000/api/products/filter/?name=Product
# GET http://127.0.0.1:8000/api/products/filter/?id=1&name=Product

]
