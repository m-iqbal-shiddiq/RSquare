from django import forms

from .models import Pesanan
from home.models import Product
from django.core.validators import RegexValidator

class FormPesanan(forms.ModelForm):
    id_product = forms.IntegerField(label='id_product')
    nama = forms.CharField(label='nama', max_length=20)
    no_wa = forms.CharField(label='no_wa', max_length=12)
    title = forms.CharField(label='title', max_length=20)
    price = forms.DecimalField(label='price', decimal_places=2,max_digits=10)
    catatan = forms.CharField(label='catatan', max_length=20)
    alamat = forms.CharField(label='alamat', max_length=20)

    class Meta:
         model = Pesanan
         fields = ['id_product','nama','no_wa','title','price','catatan','alamat']