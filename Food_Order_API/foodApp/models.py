from django.db import models
from account.models import User
from django.utils import timezone
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

    def __str__(self):
        return self.dish_name

# class CartItems(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)