from django import forms

from .models import Pesanan

class CreatePesanan(forms.ModelForm):
    class Meta:
        model = Pesanan
        fields = ['nama',
                  'no_wa',
                  'title',
                  'price'
                  ]