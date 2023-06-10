from django.shortcuts import render,HttpResponse,redirect
from .models import Product,items,Cart,contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def home(request):
    product = Product.objects.all()
    context={'products':product}
    return render(request, 'home.html',context)

def Shop(request):
    allitems = items.objects.all()
    if request.method == 'GET':
        pt=request.GET.get('search')
        if pt!=None:
            allitems=Product.objects.filter(title=pt)
    it={'item':allitems}
    return render(request,'shop.html',it)

def Signup(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse('password and confirm password are incorrect !!')
        else:
            my_user=User.objects.create_user(name,email,pass1)
            my_user.save()
            return redirect('Login')
    return render(request,'signup.html')

def Login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        pass1=request.POST.get('pass')

        user=authenticate(request,email=email,password=pass1)
        if user is not None:
            auth_login(request,user)
            return redirect('signup')
        else:
            return HttpResponse("Email and password is incorrect")  
    return render(request,'Login.html')

def Contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        phone_number=request.POST.get('phone')
        email=request.POST.get('email')
        message=request.POST.get('message')
        en=contact(Name=name,Phone_numbe=phone_number,Email=email,Message=message)
        en.save()
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def add_to_cart(request):
    product = Product.objects.get(Product)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.products.add(product)
    return redirect('cart')

def carts(request):
    cart=Cart.objects.get(user=request.user)
    s={'pro':cart}
    return render(request,'cart.html',s)
