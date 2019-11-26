from django.shortcuts import render
from django.views.generic import TemplateView
from formpesanan.forms import FormPesanan
from formpesanan.models import Pesanan
from django.http import HttpResponseRedirect
# Create your views here.
class ListPesananView(TemplateView):
    template_name = 'listpesanan.html'

    def get(self, request):
        pesanan = Pesanan.objects.all()
        args = {'pesanans':pesanan}
        print(pesanan)
        return render(request, self.template_name, args)

    def hapuspesanan(self,pk):
        pesanan = Pesanan.objects.get(id=pk)
        pesanan.delete()
        return HttpResponseRedirect("/listpesanan/")