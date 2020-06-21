from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse('shop home')
    return render(request,'shop/index.html')

def about(request):
    # return HttpResponse('about shop home')
    return render(request,'shop/about.html')

def services(request):
    # return HttpResponse('services shop home')
    return render(request,'shop/services.html')

def contact(request):
    # return HttpResponse('contact shop home')
    return render(request,'shop/contactus.html')

def tracker(request):
    # return HttpResponse('tracker shop home')
    return render(request,'shop/tracker.html')


def productview(request):
    # return HttpResponse('product view shop home')
    return render(request,'shop/productview.html')

def search(request):
    # return HttpResponse('search shop home')
    return render(request,'shop/search.html')

def checkout(request):
    # return HttpResponse('checkout shop home')
    return render(request,'shop/checkout.html')