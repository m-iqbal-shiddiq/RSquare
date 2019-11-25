
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Product
from django.urls import reverse

def ProductDetail(request,pk):
    produk = Product.objects.get(id=pk)
    return render(request, 'home/product.html', {'product': produk})

def passidpesanan(request, pk):
    produk = Product.objects.get(id=pk)
    print(produk)
    return render(request, 'formpesanan/formpesanan.html', {'product':produk})
