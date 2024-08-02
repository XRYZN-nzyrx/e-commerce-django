from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *

def index(request):
    user_data = request.session.get('current_user', {})
    return render(request,'index.html', {'current_user': user_data})
def error_404(request):
    return render(request, '404.html')

def cart(request):
    user_data = request.session.get('current_user', {})
    user = User.objects.filter(email = user_data['email'], name = user_data['name']).first()
    cart = Cart.objects.filter(user = user).first()
    # addProds(cart=cart)
    print(cart.products.all())
    return render(request, 'cart.html', {'products': cart.products.all()})
def addProds(cart):
    products = Product.objects.all()
    for product in products:
        CartProduct.objects.create(cart=cart, product=product, quantity=5)
def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')


def shop_detail(request):
    return render(request, 'shop-detail.html')

def shop(request):
    return render(request, 'shop.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def login(request):
    return render(request,'login.html')
def log(request):
    a = request.GET['email']
    b = request.GET['password']
    if User.objects.filter(email=a,password=b):
        user = User.objects.filter(email=a, password = b).first()
        print(user)
        request.session['current_user'] = {
            'name': user.name,
            'email': user.email
        }
        return redirect("../")
    else:
        return redirect('../login.html/')  

def logout(request):
    try:
        del request.session["current_user"]
    except KeyError:
        pass
    return redirect('../')

def signup(request):
    return render(request,'signup.html')
def sign(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        
        u = User(name=name, email=email, password=password, phone_number=phone_number)
        u.save()
        cart = Cart(
            user = u
        )
        cart.save()
        messages.success(request, 'Account created successfully!')
        return redirect('../login.html/') 
    
    return redirect('../signup/')

