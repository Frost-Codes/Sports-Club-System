from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField
from .info import *

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    current_price = models.FloatField()
    previous_price = models.FloatField()
    flash_sale = models.BooleanField(default=False)
    in_stock = models.IntegerField()
    description = models.TextField()
    category = models.CharField(choices=CHOICES, max_length=2)
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.title


class CustomerDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    next_of_kin = models.CharField(choices=NEXT_OF_KIN, max_length=10)
    next_of_kin_contact = models.IntegerField()
    date_of_birth = models.DateField()
    contact = models.IntegerField()
    sub_county = models.CharField(choices=SUB_COUNTIES, max_length=50)
    school = models.CharField(max_length=300)
    games_of_interest = MultiSelectField(choices=GAMES, max_length=100, max_choices=20)
    height_in_cm = models.IntegerField()
    weight_in_kgs = models.IntegerField()
    special_needs = models.CharField(choices=SPECIAL_NEEDS, max_length=3)

    def __str__(self):
        return self.first_name


class County(models.Model):
    county = models.CharField(choices=COUNTIES, max_length=50)

    def __str__(self):
        return self.county


class Town(models.Model):
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    town = models.CharField(choices=TOWNS, max_length=50)
    shipping_cost = models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.town


class CustomerAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    pick_up_station = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    contact = models.IntegerField()

    def __str__(self):
        return self.pick_up_station


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.current_price


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)



