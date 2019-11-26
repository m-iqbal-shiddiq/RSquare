
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Product
from formpesanan.forms import FormPesanan
from django.urls import reverse

def ProductDetail(request,pk):
    produk = Product.objects.get(id=pk)
    return render(request, 'home/product.html', {'product': produk})

def passidpesanan(request, pk):
    produk = Product.objects.get(id=pk)
    form = FormPesanan
    return render(request, 'formpesanan/formpesanan.html', {'product':produk, 'form':form})

def post(request):
        form = FormPesanan(request.POST)
        if form.is_valid():
            nama = form.cleaned_data['nama']
        else:
            print('form tidak valid')
            print(form)
        args = {'form':form, 'nama':nama}
        return render(request, 'home/finishpesanan.html', args)

