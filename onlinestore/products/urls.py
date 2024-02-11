
from django.urls import include, path

from . import views

urlpatterns = [
    path('products/', views.product_list , name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
    path('manufacturers/', views.manufacturers_list, name='manufacturers-list'),
    path('manufacturers/<int:pk>/', views.manufacturer_detail, name='manufacturer-detail'),

]
