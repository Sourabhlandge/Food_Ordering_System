from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Restaurant(models.Model):
    #restaurent
    restaurant_name = models.CharField(max_length=100)
    restaurant_location = models.CharField(max_length=100)
    restaurant_contact_no = models.CharField(max_length=100)

    def __str__(self):
        return self.restaurant_name
class Item(models.Model):
    res_name = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    dish_name = models.CharField(max_length=150)
    description = models.CharField(max_length=250,blank=True)
    price = models.FloatField()
    image = models.ImageField(default='default.png', upload_to='images/')
    
    def __str__(self):
        return self.dish_name



class CartItems(models.Model):
    ORDER_STATUS = (
        ('Active', 'Active'),
        ('Delivered', 'Delivered')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    ordered_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='Active')
    delivery_date = models.DateField(default=timezone.now)

    # address = models.CharField(max_length=256)
    # contact_no = models.IntegerField()
    # pin_code = models.IntegerField()


    def __str__(self):
        return self.item.dish_name

class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    address = models.CharField(max_length=256)
    contact_no = models.IntegerField()
    pin_code = models.IntegerField()       

    def __str__(self):
        return self.address   
