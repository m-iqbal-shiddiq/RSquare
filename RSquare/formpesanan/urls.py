from django.urls import path
from .views import CreatePesananView
app_name='formpesanan'
urlpatterns = [
    path('product/12/formpesanan', CreatePesananView.as_view(), name='formpesanan'),
    # path(r'^submitpesanan', CreatePesananView.post, name='passidpesanan')
]