from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *


def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def log(request):
    if request.method == 'POST':
       
        a = request.POST.get('email')  
        b = request.POST.get('password')
        if User.objects.filter(email=a,password=b):
            return render(request,'home.html')
        else:
            return render(request,'login.html')  
    return HttpResponse("Invalid request method")


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
        
        messages.success(request, 'Account created successfully!')
        return redirect('login') 
    
    return redirect('signup')

