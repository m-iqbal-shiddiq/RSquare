from django import forms

class CreatePesanan(forms.ModelForm):
    class Meta:
        fields = ['title','sku','short_description','price','image']