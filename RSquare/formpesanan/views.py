from django.shortcuts import render
from . import forms
from home.models import Product
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import CreatePesanan
from .models import Pesanan
# Create your views here.

class CreatePesananView(CreateView):
    template_name = 'formpesanan.html'
    queryset = Pesanan.objects.all()
    form_class = CreatePesanan

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def pesanan_create(request,id):
        product = Product.objects.get(id=id)
        form = forms.CreatePesanan(instance=product)
        return render(request, '/', {'product':product})