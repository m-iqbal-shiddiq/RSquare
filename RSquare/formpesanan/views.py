from django.shortcuts import render
from . import forms
from home.models import Product
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import FormPesanan
from .models import Pesanan
# Create your views here.

class CreatePesananView(CreateView):
    template_name = 'formpesanan.html'
    queryset = Pesanan.objects.all()
    form_class = FormPesanan

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def pesanan_create(request,id):
        product = Product.objects.get(id=id)
        form = forms.FormPesanan(instance=product)
        return render(request, '/', {'product':product})

    def get(self,request):

        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = FormPesanan(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponseRedirect('/thanks/')

            # if a GET (or any other method) we'll create a blank form
        else:
            form = FormPesanan()
        print(form.price)
        return render(request, self.template_name, {'form': form})

    def post(self,request):
        form = FormPesanan(request.POST)
        if form.is_valid():
            nama = form.cleaned_data['nama']
        args = {'form':form, 'nama':nama}
        return render(request, 'formpesanan/formpesanan.html', args)

