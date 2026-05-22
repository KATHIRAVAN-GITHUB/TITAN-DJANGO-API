from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.get_products),
    path('products/<int:id>/', views.get_product_by_id),
    path('products/add/', views.add_product),
]