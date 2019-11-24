from django.shortcuts import render
from . import forms
from django.views.generic import TemplateView
# Create your views here.

class CreatePesananView(TemplateView):
    template_name = 'formpesanan.html'


def pesanan_create(request,sku_produk):
    form = forms.CreatePesanan(instance=produk)
    return render(request, 'formpesanan/formpesanan.html', {'form':form })