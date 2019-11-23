from django.urls import path
from .views import ListPesananView

urlpatterns = [
   path('', ListPesananView.as_view(template_name = "ListPesanan/listpesanan.html"), name='contact')
]