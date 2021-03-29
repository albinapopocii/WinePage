from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    firstName = models.CharField(max_length=200, null=True)
    lastName = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.firstName


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    origin = models.CharField(max_length=200, null=True)
    dimension = models.FloatField(null=True)
    price = models.FloatField(null=True)
    alcohol = models.FloatField(null=True)
    taste = models.CharField(max_length=200, null=True)
    little_description = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=4000, null=True)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def delivery(self):
        delivery = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                delivery = True
        return delivery

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class DeliveryOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=False)
    phoneNumber = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

    def __str__(self):
        return self.phoneNumber


class Article(models.Model):
    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=1000, null=True)
    description = models.CharField(max_length=20000, null=True)
    information = models.CharField(max_length=20000, null=True)
    link = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Event(models.Model):
    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=1000, null=True)
    description = models.CharField(max_length=20000, null=True)
    place = models.CharField(max_length=50, null=True)
    date = models.CharField(max_length=15, null=True)
    time = models.CharField(max_length=20, null=True)
    price = models.FloatField(max_length=20, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url