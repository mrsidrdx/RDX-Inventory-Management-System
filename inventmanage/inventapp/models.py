from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

class Inventory(models.Model):
    inv_id = models.PositiveIntegerField()
    inv_name = models.CharField(max_length=100)
    inv_location = models.CharField(max_length=100)

    def __str__(self):
        return self.inv_name

class Item(models.Model):
    item_id = models.PositiveIntegerField()
    item_stock = models.PositiveIntegerField()
    item_minimum_required = models.PositiveIntegerField()
    item_name = models.CharField(max_length=100)
    inv = models.PositiveIntegerField()

    def __str__(self):
        return self.item_name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    users_id = models.PositiveIntegerField(default=301)
    mobile_regex = RegexValidator(regex=r'^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[6789]\d{9}|(\d[ -]?){10}\d$', message="Please Enter A Valid Mobile Number!")
    user_mobile = models.CharField(validators=[mobile_regex], max_length=10)
    inv_id = models.ForeignKey(Inventory, on_delete = models.CASCADE, related_name='inventory_user')

    def __str__(self):
        return self.user.username

class Customer(models.Model):
    customer_id = models.PositiveIntegerField()
    customer_name = models.CharField(max_length=100)
    mobile_regex = RegexValidator(regex=r'^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[6789]\d{9}|(\d[ -]?){10}\d$', message="Please Enter A Valid Mobile Number!")
    customer_mobile = models.CharField(validators=[mobile_regex], max_length=10)
    customer_email = models.EmailField()
    users = models.PositiveIntegerField()

    def __str__(self):
        return self.customer_name

class Payment(models.Model):
    pay_id = models.PositiveIntegerField()
    pay_date = models.DateField()
    pay_amount = models.PositiveIntegerField()
    customer = models.PositiveIntegerField()
    users = models.PositiveIntegerField()

    def __str__(self):
        return str(self.pay_id)

class Orders(models.Model):
    order_id = models.PositiveIntegerField()
    pay = models.PositiveIntegerField()
    customer = models.PositiveIntegerField()
    users = models.PositiveIntegerField()
    item = models.PositiveIntegerField()

    def __str__(self):
        return str(self.order_id)
