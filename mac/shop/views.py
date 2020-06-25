from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
from math import ceil
from datetime import datetime
from django.contrib import messages

# Create your views here.

def index(request):

    # return HttpResponse('shop home')
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # print(n)
    # nSlides = n // 4 + ceil((n / 4)-(n // 4))
    # params = {'no_of_slides':nSlides , 'range':range(1,nSlides),'product':products}
    
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1,nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request,'shop/index.html',params)

def about(request):
    # return HttpResponse('about shop home')
    return render(request,'shop/about.html')

def services(request):
    # return HttpResponse('services shop home')
    return render(request,'shop/services.html')

def contact(request):
    # return HttpResponse('contact shop home')
    if request.method=="POST":
      name=request.POST.get("name")
      email=request.POST.get("email")
      phone=request.POST.get("phone")
      desc=request.POST.get("desc")
      contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
      contact.save()
      messages.success(request, 'Your Message has been sent!.') 
    return render(request,'shop/contact.html')

def tracker(request):
    # return HttpResponse('tracker shop home')
    return render(request,'shop/tracker.html')


def productview(request,myid):
    # return HttpResponse('product view shop home')
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request,'shop/productview.html',{'product':product[0]})

def search(request):
    # return HttpResponse('search shop home')
    return render(request,'shop/search.html')

def checkout(request):
    # return HttpResponse('checkout shop home')
    return render(request,'shop/checkout.html')