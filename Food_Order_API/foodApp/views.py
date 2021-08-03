from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.db.models import Sum    

class RestaurantAPI(APIView):
    #Retrieve
    def get(self, request):
        qs = Restaurant.objects.all()
        ser = RestaurantSerializer(qs, many=True)
        return Response(ser.data)

    #Create
    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Update
    def put(self, request):
        id = request.POST.get("id")        
        restaurant_name = request.POST.get("restaurant_name")        
        restaurant_location = request.POST.get("restaurant_location")        
        restaurant_contact_no = request.POST.get("restaurant_contact_no")        
        try:
            qs = Restaurant.objects.get(id=id)
            if qs:
                qs.restaurant_name = restaurant_name
                qs.restaurant_location = restaurant_location
                qs.restaurant_contact_no = restaurant_contact_no
                qs.save()
                resp = {
                    'success' : 'true',
                    'message' : "Successfully Updated",
                }
                return Response(resp, status=status.HTTP_201_CREATED)
        except:       
            resp = {
                'success' : 'false',
                'message' : "Something went wrong try again",      
                }    
            return Response(resp, status=status.HTTP_304_NOT_MODIFIED) 
    #Delete
    def delete(self, request):
        id = request.POST.get("id")  
        try:           
            qs = Restaurant.objects.get(id=id).delete()
            if qs:
                resp = {
                    'success' : 'true',
                    'message' : "Restaurant Deleted",
                }
                return Response(resp, status=status.HTTP_200_OK)
        except:
            resp = {
                'success' : 'false',
                'message' : "Record does not exist",        }    
            return Response(resp, status=status.HTTP_400_BAD_REQUEST) 

class ItemAPI(APIView):
    #Retrieve Item    
    def get(self, request):
        id = request.POST.get("id") 
        qs = Item.objects.filter(res_name=id)
        ser = ItemSerializer(qs, many=True)
        return Response(ser.data)

    #Create Item
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Update Item
    def put(self, request):
        id = request.POST.get("id")       
        dish_name = request.POST.get("dish_name")
        description = request.POST.get("description")
        price = request.POST.get("price")    
        try: 
            qs = Item.objects.get(id=id)
            if qs:
                qs.dish_name = dish_name
                qs.description = description
                qs.price = price
                qs.save()
                resp = {
                    'success' : 'true',
                    'message' : "Item Has Been Successfully Updated",
                }
                return Response(resp, status=status.HTTP_201_CREATED)
        except:
            resp = {
                'success' : 'false',
                'message' : "Something went wrong try again",      
                }    
            return Response(resp, status=status.HTTP_304_NOT_MODIFIED) 

    #Delete Item
    def delete(self, request):
        id = request.POST.get("id")  
        try:           
            qs = Item.objects.get(id=id).delete()
            if qs:
                resp = {
                    'success' : 'true',
                    'message' : "Item Deleted",
                }
                return Response(resp, status=status.HTTP_200_OK)
        except:
            resp = {
                'success' : 'false',
                'message' : "Record does not exist",        }    
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)        

                  

# class CartAPI(APIView):
#     #Add to cart
#     def post(request):
#         menu_Id = request.POST.get("id")
#         item = Item.objects.filter(id=menu_Id)
#         # #item = get_object_or_404(Item, id=id)
#         cart_item = CartItems.objects.create(
#               item=item,
#               user=request.user,
#         # #     ordered=False,
#           )
#         #cart_items = CartItems.objects.filter(user=request.user)
#         serializer = CartSerializer(cart_item,many=True)
#         if serializer.is_valid():
#             serializer.save()
               