from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from djstripe.models import Product

def homepage(request):
    return render(request, "home.html")

@login_required
def checkout(request):
    products = Product.objects.all()
    return render(request,"base/checkout.html",{"products": products})