from django.db.models import query
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Cart, Category, Customer, Image, Order, OrderItem, Product, Sale, Size, Transaction, WishList
from .serializers import (CartSerializer, CategorySerializer,
                          CustomerSerializer, ImageSerializer, OrderItemSerializer, OrderSerializer, ProductSerializer,
                          SaleSerializer, SizeSerializer, TransactionSerializer, WishListSerializer)


@api_view(['GET'])
def index(request, format=None):
    if request.method == 'GET':
        sales = Sale.objects.all()
        salesSerializer = SaleSerializer(sales, many=True)
        return Response({ 'sales': salesSerializer.data }, status=status.HTTP_200_OK)


@api_view(['GET'])
def sizes(request, format=None):
    sizes = Size.objects.all()
    serializer = SizeSerializer(sizes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def sales(request, format=None):
    sales = Sale.objects.all()
    serializer = SaleSerializer(sales, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def images(request, format=None):
    images = Image.objects.all()
    imageSerializer = ImageSerializer(images, many=True)
    return Response(imageSerializer.data, status=status.HTTP_200_OK)

class CategoryDetails(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class Categories(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.prefetch_related('images').all()
    serializer_class = ProductSerializer


class Products(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CustomerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class Customers(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class Orders(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderItems(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class TransactionDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class Transactions(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class CartDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class Carts(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class WishListDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer


class WishLists(generics.ListCreateAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
