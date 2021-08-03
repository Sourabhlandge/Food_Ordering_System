from django.db.models import fields
from rest_framework import serializers
from .models import *

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         models = CartItems
#         fields = "__all__"        