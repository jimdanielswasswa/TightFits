from django.shortcuts import resolve_url
from django.urls import path
from .views import (CartDetails, Carts, CategoryDetails, Categories, CustomerDetails, Customers, OrderDetails, OrderItemDetails, OrderItems, Orders,
                    TransactionDetails, Transactions, WishListDetails, WishLists, images, index, ProductDetail, Products, sales, sizes)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path(route='', view=index, name='index'),
    path(route='categories/<int:pk>/',
         view=CategoryDetails.as_view(), name='category'),
    path(route='categories/', view=Categories.as_view(), name='categories'),
    path(route='sizes/', view=sizes, name='sizes'),
    path(route='products/<int:pk>/', view=ProductDetail.as_view(), name='product'),
    path(route='products/', view=Products.as_view(), name='products'),
    path(route='sales/', view=sales, name='sales'),
    path(route='customers/<int:pk>',
         view=CustomerDetails.as_view(), name='customer'),
    path(route='customers/', view=Customers.as_view(), name='customers'),
    path(route='orders/<int:pk>', view=OrderDetails.as_view(), name='order'),
    path(route='orders/', view=Orders.as_view(), name='orders'),
    path(route='order-items/<int:pk>',
         view=OrderItemDetails.as_view(), name='orderitem'),
    path(route='order-items/', view=OrderItems.as_view(), name='orderitems'),
    path(route='transactions/<int:pk>',
         view=TransactionDetails.as_view(), name='transaction'),
    path(route='transactions/', view=Transactions.as_view(), name='transactions'),
    path(route='carts/<int:pk>', view=CartDetails.as_view(), name='cart'),
    path(route='carts/', view=Carts.as_view(), name='carts'),
    path(route='wishlists/<int:pk>', view=WishListDetails.as_view(), name='wishlist'),
    path(route='wishlists/', view=WishLists.as_view(), name='wishlist'),
    path(route='images/', view=images, name='images'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
