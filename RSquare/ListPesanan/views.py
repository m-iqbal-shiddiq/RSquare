from django.shortcuts import render
from django.views.generic import TemplateView
from formpesanan.forms import FormPesanan
from formpesanan.models import Pesanan
# Create your views here.
class ListPesananView(TemplateView):
    template_name = 'listpesanan.html'

    def get(self, request):
        pesanan = Pesanan.objects.all()
        args = {'pesanans':pesanan}
        print(pesanan)
        return render(request, self.template_name, args)