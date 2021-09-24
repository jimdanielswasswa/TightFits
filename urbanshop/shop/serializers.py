from django.db.models import fields
from rest_framework import serializers
from .models import Image, Size, Category, Product, Sale, Customer, Order, OrderItem, Transaction, Cart, WishList


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'size']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'image']


class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many = True, queryset=Category.objects.all())
    class Meta:
        model = Product
        ordering = ['-id']
        fields = ['id', 'name', 'description', 'price', 'size', 'categories', 'image', 'images']


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'product', 'price', 'start_date', 'end_date']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone_number', 'address1', 'address2', 'city',
            'state', 'zip', 'created_at', 'updated_at'
        ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'created_by', 'total', 'shipping_cost',
                  'credit_card_number', 'created_at']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product',
                  'quantity', 'unit_price', 'shipping_date']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'order', 'type', 'amount', 'response_code',
                  'response_reason', 'response', 'transaction_id', 'created_at']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user_session_id', 'product',
                  'quantity', 'created_at', 'updated_at']


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ['id', 'user_session_id', 'product',
                  'quantity', 'created_at', 'updated_at']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [ 'id', 'image', 'tag' ]