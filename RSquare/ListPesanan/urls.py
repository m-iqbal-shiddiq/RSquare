from django.urls import path
from .views import ListPesananView
app_name = 'listpesanan'
urlpatterns = [
   path('', ListPesananView.as_view(template_name = "ListPesanan/listpesanan.html"), name='contact'),
   path('<pk>', ListPesananView.hapuspesanan, name='deletepesanan')
]