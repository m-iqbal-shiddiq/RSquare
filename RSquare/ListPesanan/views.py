from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ListPesananView(TemplateView):
    template_name = 'listpesanan.html'