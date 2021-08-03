from django.urls import path,include
from foodApp import views as v1

app_name = "foodApp"

urlpatterns = [
    path('', v1.showRestaurant, name="home"),
    path('getitem/', v1.getItem, name="item"),
    path('signup/',v1.signup_view),
    path('logout/',v1.logout_view),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add-to-cart/<int:id>/', v1.add_to_cart, name='add-to-cart'),
    path('cart/', v1.get_cart_items, name='cart'),
    path('cart_remove/', v1.cart_remove),
    path('ordered/', v1.order_item, name='ordered'),
    path('order_details/', v1.order_details, name='order_details'),
]