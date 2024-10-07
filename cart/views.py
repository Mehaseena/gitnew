from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user=User.objects.create_user(username=username, email=email, password=password)
        user.save()

        login(request,user)
        return redirect('login')
    return render(request, 'cart/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('admin_view')
            else:
                return redirect('home')
        else:
            return redirect('login')

    return render(request, 'cart/login.html')

def admin_view(request):
    if not request.user.is_superuser:
        return redirect('home')  
    return render(request, 'cart/admin.html')

def home(request):
     return render(request,'cart/index.html')

from django.shortcuts import render, redirect
from .models import Product, CartItem, Order
from django.http import HttpResponse


def product_list(request):
	products = Product.objects.all()
	return render(request, 'cart/product_list.html', {'products': products})


def product_details(request,id):
     product=Product.objects.get(id=id)
     return render(request,'cart/product_detail.html',{'product':product})


def view_cart(request):
	cart_items = CartItem.objects.filter(user=request.user)
	total_price = sum(item.product.price * item.quantity for item in cart_items)
	return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    
    try:
        cart_item = CartItem.objects.get(product=product, user=request.user)
        cart_item.quantity += 1  # If the item exists, increment the quantity
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, user=request.user, quantity=1)
    
    cart_item.save()
    return redirect('product_list')



def remove_from_cart(request, item_id):
	cart_item = CartItem.objects.get(id=item_id)
	cart_item.delete()
	return redirect('view_cart')


def place_order(request):
    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items.exists():
        return redirect('product_list')

    existing_order = Order.objects.filter(user=request.user).first()

    if request.method == 'POST':
        address = request.POST.get('address')

        if existing_order:
            existing_order.address = address
            existing_order.save()
        else:
            order = Order.objects.create(user=request.user, address=address)

        cart_items.delete()
        

        return redirect('order_confirmation')

    return render(request, 'cart/place_order.html', {
        'cart_items': cart_items,
        'user': request.user,  
        'existing_address': existing_order.address if existing_order else '' 
    })


def order_confirmation(request):
    return render(request, 'cart/order_confirmation.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category
from .forms import CategoryForm

def create_category(request):
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = CategoryForm()

    return render(request, 'cart/create_category.html', {'form': form})

from .models import Product
from .forms import ProductForm

def create_product(request):
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()

    return render(request, 'cart/create_product.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect, render
from .models import Product

def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    
    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.save()
        return redirect('product_list')
    
    return render(request, 'cart/edit_product.html', {'product': product})


from django.shortcuts import get_object_or_404, redirect
from .models import Product

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    
    return redirect('product_list')



 