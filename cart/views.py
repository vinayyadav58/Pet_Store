# from django.shortcuts import render,redirect
# from petsapp.models import pet
# from .models import cart
# from django.contrib import messages
# from django.http import JsonResponse
# from django.db.models import F,Sum


# # Create your views here.

# def add_to_cart(request,id):
#     cart_id = request.session.session_key
#     if cart_id == None:
#         cart_id = request.session.create()

#     pet_data = pet.objects.get(id=id)
#     Price = pet_data.price
#     user = request.user

#     cart(cart_id=cart_id,pet=pet_data,user=user,totalprice=Price).save()
#     messages.success(request," Item added to cart succesfully ")
#     return redirect ("/")

# def cart_home(request):
#     all_items = cart.objects.filter(user=request.user)
#     flag = all_items.exists()
#     return render(request,'cart/cart_home.html',{'items' : all_items,'flag':flag})

# def delete_cart_product(request,id):
#     Cart = cart.objects.get(id=id)
#     Cart.delete()
#     messages.success(request," item removed from cart ")
#     return redirect("carthome")

# def update_cart(request,id):
#     p = request.POST.get('price')
#     q = request.POST.get('qty')
#     p_id = request.POST.get('id')
#     totalprice = float(p) * int(q)
#     cart.objects.filter(id=p_id).update(quantity=q,totalprice=totalprice)
#     # total = cart.objects.filter(user=request.user).aggregate(totalprice=Sum(F('totalprice') * F('quantity')))
#     # totalamount = total['totalprice'] or 0.0
#     # return JsonResponse({'status':True,'totalprice':totalprice,'totalam':totalamount})
#     total_amount = cart.objects.filter(user=request.user).aggregate(total=Sum('totalprice'))['total'] or 0.0
#     print('TA',total_amount)
#     return JsonResponse({'status':True,'totalprice':totalprice,'totalamount':total_amount})

from django.shortcuts import render,redirect
from petsapp.models import pet
from .models import cart
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import F,Sum


# Create your views here.

def add_to_cart(request,id):
    cart_id = request.session.session_key
    if cart_id == None:
        cart_id = request.session.create()

    pet_data = pet.objects.get(id=id)
    Price = pet_data.price
    user = request.user

    cart(cart_id=cart_id,pet=pet_data,user=user,totalprice=Price).save()
    messages.success(request," Item added to cart succesfully ")
    return redirect("/")


def cart_home(request):
    all_items = cart.objects.filter(user=request.user)
    flag = all_items.exists()
    return render(request,'cart/cart_home.html',{'items' : all_items,'flag':flag})



def delete_cart_product(request,id):
    Cart = cart.objects.get(id=id)
    Cart.delete()
    messages.success(request," item removed from cart ")
    return redirect("carthome")


def update_cart(request,id):
    p = request.POST.get('price')
    print('Price',p)
    q = request.POST.get('qty')
    print('quantity',q)
    p_id = request.POST.get('id')
    totalprice = float(p) * int(q)
    print('total',totalprice)
    cart.objects.filter(id=p_id).update(quantity=q,totalprice=totalprice)
    total_amount = cart.objects.filter(user=request.user).aggregate(total=Sum('totalprice'))['total'] or 0.0
    print('TA',total_amount)
    return JsonResponse({'status':True,'totalprice':totalprice,'totalamount':total_amount})
    # totalamount = total['totalprice'] or 0.0
    # return JsonResponse({'status':True,'totalprice':totalprice,'totalam':totalamount})