from django.urls import path
from .views import RestaurantAPI, ItemAPI

urlpatterns = [
    path('res/', RestaurantAPI.as_view() ),
    path('item/', ItemAPI.as_view() ),
   # path('cart/', CartAPI.as_view() ),
]