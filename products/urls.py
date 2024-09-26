from django.urls import path
from . import views

urlpatterns = [
    path('add-product/', views.add_product_view, name='add_product'),
    path('products/', views.product_list_view, name='product_list'),
]
