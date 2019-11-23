from django.urls import path
from .views import ContactView

urlpatterns = [
   path('', ContactView.as_view(template_name = "contact/contact.html"), name='contact')
]