from django.db import models
from django.db.models.fields.reverse_related import OneToOneRel
from cloudinary.models import CloudinaryField

class Image(models.Model):
    image = CloudinaryField('image', null=True, format="jpg")
    tag = models.CharField(max_length=50, null=False, default='')
    def __str__(self):
        return f"{self.tag} : {self._id}"

class Size(models.Model):
    size = models.CharField(max_length=40, blank=False)

    def __str__(self):
        return f"{self.size} : {self._id}"


class Category(models.Model):
    name = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length=200, blank=False)
    image = CloudinaryField('image', null=True, format='jpeg', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True)

    def __str__(self):
        return f"{self.name} : {self._id}"


class Product(models.Model):
    name = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length=200, blank=False)
    price = models.IntegerField(blank=False)
    categories = models.ManyToManyField(to=Category, related_name='categories')
    size = models.ForeignKey(to=Size, on_delete=models.DO_NOTHING, null=True)
    image = CloudinaryField('image', null=True, format="jpg")
    images = models.ManyToManyField(to=Image, related_name='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True)

    def __str__(self):
        return f"{self.name} : {self._id}"

class Sale(models.Model):
    product = models.OneToOneField(
        to=Product, to_field='_id', on_delete=models.CASCADE, null=True)
    price = models.IntegerField(blank=False)
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.start_date} : {self._id} : {self.end_date}"


class Customer(models.Model):
    first_name = models.CharField(max_length=16, blank=False)
    last_name = models.CharField(max_length=16, blank=False)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=15)
    address1 = models.CharField(max_length=80, blank=False)
    address2 = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=20)
    zip = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name} : {self._id}"


class Order(models.Model):
    created_by = models.ManyToOneRel(
        to=Customer, field=models.ForeignKey, field_name='customer')
    total = models.IntegerField(blank=False)
    shipping_cost = models.IntegerField(blank=False)
    credit_card_number = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.created_by} : {self._id}"


class OrderItem(models.Model):
    order = models.ManyToOneRel(
        to=Order, field=models.ForeignKey, field_name='order')
    product = models.OneToOneRel(
        to=Product, field=models.ForeignKey, field_name='product')
    quantity = models.IntegerField(blank=False)
    unit_price = models.IntegerField(blank=False)
    shipping_date = models.DateTimeField(blank=False)


class Transaction(models.Model):
    order = models.OneToOneRel(
        to=Order, field=models.ForeignKey, field_name='order')
    type = models.CharField(max_length=18, blank=False)
    amount = models.IntegerField(blank=False)
    response_code = models.IntegerField()
    response_reason = models.CharField(max_length=100)
    response = models.CharField(max_length=100)
    transaction_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    user_session_id = models.CharField(max_length=32, blank=False)
    product = models.OneToOneRel(
        to=Product, field=models.ForeignKey, field_name='product')
    quantity = models.IntegerField(blank=False, null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()


class WishList(models.Model):
    user_session_id = models.CharField(max_length=32, blank=False)
    product = models.OneToOneRel(
        to=Product, field=models.ForeignKey, field_name='product')
    quantity = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()