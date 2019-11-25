from django.shortcuts import render
from . import forms
from home.models import Product
from django.views.generic import TemplateView
# Create your views here.

class CreatePesananView(TemplateView):
    template_name = 'formpesanan.html'

    def pesanan_create(request,id):
        product = Product.objects.get(id=id)
        form = forms.CreatePesanan(instance=product)
        return render(request, 'formpesanan/formpesanan.html', {'product':product})