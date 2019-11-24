from django.urls import path
from .views import CreatePesananView

urlpatterns = [
   path('', CreatePesananView.as_view(template_name = "formpesanan/formpesanan.html"), name='formpesanan')
]