from django.urls import path

from .views import (products, product, create_product,
                    edit_product, delete_product, search,)

app_name = "products"

urlpatterns = [
    path('', products, name='products'),
    # path('create_product', create_product, name='create_product'),
    path('home', products, name='home'),
    path('products', products, name='products'),
    path('products/create', create_product, name='create_product'),
    path('products/<int:id>', product, name='product'),
    path('products/edit/<int:id>', edit_product, name='edit_product'),
    path('products/delete/<int:id>', delete_product, name='delete_product'),
    path('products/search/', search, name='search')

]

# CRUD OPERATAION

'''
    1) fetch all the products
    2) fetch single product
    3) create a product
    4) edit a product
    5) delete a product
'''
