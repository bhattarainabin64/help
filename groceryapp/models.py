from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Fullname = models.CharField(max_length=250)
    address = models.CharField(max_length=150, null=True, blank=True)
    join_us = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Fullname


class Category(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


# Product Model FIELD


class Product(models.Model):
    objects = None
    product_name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="Products")
    latest_market_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    desciption = models.TextField()
    count = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class Cart(models.Model):
    objects = None
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart: " + str(self.id)


class CartProduct(models.Model):
    objects = None
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    total = models.PositiveIntegerField()

    def __str__(self):
        return "Cart: " + str(self.cart.id) + "CartProduct: " + str(self.id)

order_status=(
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)




class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    order_by = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=300)
    mobile_number = models.CharField(max_length=10)
    Email = models.EmailField(null=True, blank=True)
    sub_total = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status=models.CharField(max_length=200,choices=order_status)
    created_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Order: " + str(self.id)
