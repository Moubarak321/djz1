from . import views
from django.urls import path

urlpatterns = [
    path('product/<str:slug>', views.product_detail, name="product"),
    path('product/<str:slug>/add-to-cart', views.add_to_cart, name="add-to-cart"),
    path('cart/', views.cart, name='cart'),
    path('cart/delete', views.delete_cart, name='delete-cart')
]