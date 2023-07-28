from django.shortcuts import render,get_object_or_404,redirect
from .models import*
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib import messages
from.models import User
from django.contrib.auth import authenticate, login as django_login


# Create your views here.



def home(request):
    trending = Product.objects.filter(trending=1)
    arrivals = Product.objects.filter(new_arrivals=1)
    
    
    context ={
        'trending':trending,
        'arrivals':arrivals,
        }
    return render(request, "store/home.html", context)

def category(request, cat_id):
    category = Product.objects.filter(category=cat_id)
    categories = Category.objects.all()
    products = Product.objects.all()
    page = Paginator(products, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'category':category,
        'categories':categories,
        'page':page,
    }
    
    return render(request, "store/category.html", context)

def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    page = Paginator(products, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    
    
    
    context ={
        'categories':categories,
        'page':page,
        
    }
    return render(request, "store/shop.html", context)

def productsearch(request):
    categories = Category.objects.all()
    if request.method == "POST":
        searched = request.POST['searched']
        searches = Product.objects.filter(name__contains=searched)
    
    
    context ={
        'categories':categories,
        'searched':searched,
        'searches':searches 
    }
    
    return render(request, "store/search.html", context)

def productview(request, id):
    # products = Product.objects.get(slug)
    products = get_object_or_404(Product, pk=id)
    related = Product.objects.filter(category=products.category).exclude(id=id)[:4]
    context={
        'p':products,
        'related':related,
    }
    
    
    return render(request, "store/detail.html",context)

def cartPage(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            return JsonResponse({'status': "sucess"})
        else:
            prod_id = request.POST.get('product_id')
            product_check = Product.objects.get('id=prod_id')
            if(product_check):
                if(Cart.objects.filter(product_id=prod_id)):
                    return JsonResponse({'status': "already in cart"})
                else:
                    prod_qty = int(request.POST.get('product_qty'))
                    
                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status': "product added successfully"})
                    else:
                        return JsonResponse({'status': "only"+ str(product_check.quantity) + "quantity available"})
            else:
                return JsonResponse({'status': "no product found"})
    return render(request, "store/cart.html")

def login(request):
    if request.method =='POST':
        passwd = request.POST.get('password')
        email = request.POST.get('Email')
        
        user = authenticate(request, Email=email, password=passwd)
        
        if user is not None:
            django_login(request, user)
            return redirect('register')
        else:
            messages.success(request, 'Loggedin successfully.')
            return render(request, "store/home.html") 
    return render(request, "store/login.html")

def register(request):
    msg = None
    success = False

    

    if request.method == "POST":
        Email = request.POST['Email']
        ConfirmPassword =request.POST['pass1']
        Password = request.POST['pass2']
        
        new_user = User( Email=Email, ConfirmPassword=ConfirmPassword, Password=Password)
        new_user.save()
    return render(request, "store/register.html")