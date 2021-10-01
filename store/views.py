from django.shortcuts import render, redirect
from .models import Product, Cartitem, Address
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models import Sum



def home(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        quantity__sum = Cartitem.objects.filter(user=request.user).aggregate(Sum('quantity'))['quantity__sum']
    else:       # cookies/cache
        quantity__sum = 0   
    return render(request, "store/home.html", {'products': products, 'totalitem': quantity__sum})

def product_detail(request, id):
    product = Product.objects.get(pk=id)
    return render(request, "store/productdetail.html", {'product': product})

@login_required
def add_to_cart(request):
    user_id = request.user.id
    product_id = request.GET.get('prod_id')
    is_item_exist = Cartitem.objects.filter(Q(product_id=product_id) & Q(user_id=user_id)).exists()
    if is_item_exist:
        item = Cartitem.objects.filter(Q(product_id=product_id) & Q(user_id=user_id)).first()
        item.quantity += 1
        item.save()
    else:
        product = Product.objects.get(id=product_id)
        Cartitem(user=request.user, product=product, quantity=1).save()
    messages.success(request, 'Product Added to Cart Successfully !!')
    return redirect('/')

@login_required
def cart(request):
    temp_cart_items = []
    cart_items = Cartitem.objects.filter(user=request.user)
    total_cart_price = 0
    for item in cart_items:
        total_cart_price += item.quantity * item.product.price       
        temp_cart_items.append({
            "product" : item.product, # product object
            "quantity": item.quantity, # cart product qty
            "total_price":  item.quantity * item.product.price # product total price
        }) 
    return render(request, 'store/cart.html', {
                'total_amount': total_cart_price,
                'cart_items': temp_cart_items
            })

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cartitem.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        cart_product = [
            p for p in Cartitem.objects.all() if p.user == request.user
        ]
        for p in cart_product:
            tempamount = (p.quantity * p.product.price)
            amount += tempamount
        data = {
            'quantity': c.quantity,
            'amount': amount,                  
            'totalamount': amount              
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cartitem.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        cart_product = [
            p for p in Cartitem.objects.all() if p.user == request.user
        ]
        for p in cart_product:
            tempamount = (p.quantity * p.product.price)
            amount += tempamount
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount
        }
        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cartitem.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        cart_product = [
            p for p in Cartitem.objects.all() if p.user == request.user
        ]
        for p in cart_product:
            tempamount = (p.quantity * p.product.price)
            amount += tempamount
        data = {
            'totalamount': amount
        }
        return JsonResponse(data)
    if request.user.is_authenticated:
        totalitem = len(Cartitem.objects.filter(user=request.user))
        products = Product.objects.all()
        return render(request, "store/home.html", {'products': products, 'totalitem': totalitem})

def checkout(request):
    if request.user.is_authenticated:
        totalitem = len(Cartitem.objects.filter(user= request.user))
        user = request.user
        addr = Address.objects.filter(user=user)
        cart_items = Cartitem.objects.filter(user=request.user)
        totalitem
        amount = 0.0
        shipping_amount = 70.0
        totalamount = 0.0
        cart_product = [
            p for p in Cartitem.objects.all() if p.user == request.user
        ]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.price)
                amount += tempamount
            totalamount = amount + shipping_amount
        return render(request, 'store/checkout.html', {
            'addr': addr,
            'cart_items': cart_items,
            'totalcost': totalamount,
            'totalitem': totalitem
        })

@login_required
def add_address(request):  #save in dbase
    if request.method == "POST":
        fm = Address(request.POST)
        add = Address(
            user=request.user,
            name = request.POST.get('name'),
            mobile = request.POST['mobile'],
            address = request.POST['address'],
            city = request.POST['city'],
            zipcode = request.POST['zipcode'],
            state = request.POST['state'],
            default = request.POST['default'],
            )
        add.save()
    return redirect('checkout')
