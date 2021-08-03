from django.shortcuts import render,HttpResponseRedirect,get_object_or_404,redirect
from foodApp.models import Restaurant,Item,CartItems,Address
from foodApp.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.utils import timezone
from django.db.models import Sum

# Create your views here.
@login_required
def showRestaurant(request):
    restaurant = Restaurant.objects.all()
    return render(request, "home.html",{'restaurants': restaurant})
@login_required
def getItem(request):
    id = request.GET.get("id")
    menu_Items = Item.objects.filter(res_name=id)
    return render(request, "menu.html",{'menu_Items': menu_Items})    

def signup_view(request):
    form = SignUpForm()
    if request.method == "POST":

        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request,"signup.html",{'form':form})

def logout_view(request):
    if request.method == 'POST':
            logout(request)
            return render(request,"logout.html")

@login_required
def add_to_cart(request, id):
    item = get_object_or_404(Item, id=id)
    cart_item = CartItems.objects.create(
        item=item,
        user=request.user,
        ordered=False,
    )
    messages.info(request, "Added to Cart!!Continue Shopping!!")
    return redirect("/cart")

@login_required
def get_cart_items(request):
    cart_items = CartItems.objects.filter(user=request.user,ordered=False)
    bill = cart_items.aggregate(Sum('item__price'))
    number = cart_items.aggregate(Sum('quantity'))
    total = bill.get("item__price__sum")
    count = number.get("quantity__sum")
    context = {
        'cart_items':cart_items,
        'total': total,
        'count': count,
    }
    return render(request, 'cart.html', context)     

@login_required
def order_item(request):
    address = request.POST.get("address")
    contact_no = request.POST.get("contact_no")
    pin_code = request.POST.get("pin_code")
    userOrderDetails = Address(user=request.user, address = address, contact_no = contact_no, pin_code = pin_code)
    userOrderDetails.save()
    cart_items = CartItems.objects.filter(user=request.user,ordered=False)
    ordered_date=timezone.now()
    cart_items.update(ordered = True, ordered_date = ordered_date)
    messages.info(request, "Item Ordered")
    return redirect("/order_details")

@login_required
def order_details(request):
    items = CartItems.objects.filter(user=request.user, ordered=True,status="Active").order_by('-ordered_date')
    cart_items = CartItems.objects.filter(user=request.user, ordered=True,status="Delivered").order_by('-ordered_date')
    bill = items.aggregate(Sum('item__price'))
    number = items.aggregate(Sum('quantity'))
    total = bill.get("item__price__sum")
    count = number.get("quantity__sum")
    #userOrderDetails = Address.objects.filter(user=request.user)
    context = {
        'items':items,
        'cart_items':cart_items,
        'total': total,
        'count': count,
       # 'userOrderDetails': userOrderDetails
    }
    return render(request, 'order_details.html', context)    
@login_required
def cart_remove(request):
    id = request.GET.get("id")
    cart_items = CartItems.objects.filter(user=request.user,id=id).delete()
    return redirect('/cart')

# def cart_remove(request, item_id):
#     cart = CartItems(request.user)
#     item = get_object_or_404(Item, id=item_id)

    # return redirect('/cart')