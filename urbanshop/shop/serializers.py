from rest_framework import serializers
from .models import Size, Category, Product, Sale, Customer, Order, OrderItem, Transaction, Cart, CartItem, WishList

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = [ 'íd', 'size' ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [ 'id', 'name', 'description' ]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ 'id', 'name', 'description', 'price', 'size', 'categories' ]

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = [ 'id', 'product', 'price', 'start_date', 'end_date' ]

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
        fields = [ 'id', 'created_by', 'total', 'shipping_cost', 'credit_card_number', 'created_at' ]

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [ 'id', 'order', 'product', 'quantity', 'unit_price', 'shipping_date' ]

class TransactionSerializer(serializers.Serializer):
    class Meta:
        model = Transaction
        fields = [ 'id', 'order', 'type', 'amount', 'response_code', 'response_reason', 'response', 'transaction_id', 'created_at' ]

class CartSerializer(serializers.Serializer):
    class Meta:
        model = Cart
        fields = [ 'id', 'user_session_id', 'created_at', 'updated_at' ]

class CartItemSerializer(serializers.Serializer):
    class Meta:
        model = CartItem
        fields = [ 'id', 'cart', 'product', 'quantity', 'created_at', 'updated_at' ]

class WishListSerializer(serializers.Serializer):
    class Meta:
        model = WishList
        fields = [ 'id', 'user_session_id', 'product', 'quantity', 'created_at', 'updated_at' ]
