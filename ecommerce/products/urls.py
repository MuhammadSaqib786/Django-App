# products/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/<int:product_id>/edit/', views.product_edit, name='product_edit'),
    path('products/', views.product_list, name='product_list'),
]
