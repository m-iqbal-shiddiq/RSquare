from django.urls import path
from home import views
from formpesanan.views import  CreatePesananView
app_name='home'
urlpatterns = [
   path(r'<pk>/formpesanan', views.passidpesanan, name='passidpesanan'),
    path('<pk>', views.ProductDetail, name='ProductDetail')
]