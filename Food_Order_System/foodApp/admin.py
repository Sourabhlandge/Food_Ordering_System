from django.contrib import admin
from foodApp.models import Restaurant,Item,CartItems,Address

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(CartItems)
admin.site.register(Address)