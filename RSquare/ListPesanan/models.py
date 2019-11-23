"""List Pesanan"""

from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page


# Create your models here.

class ListPesananPage(Page):
    template = "ListPesanan/listpesanan.html"

    #content

    #pemesan
    no_wa = models.IntegerField(null=False, blank=False)
    nama = models.CharField(max_length = 100, null=False, blank=False)
    alamat = models.CharField(max_length = 100, null=False, blank=False)
    email = models.CharField(max_length = 100, null=False, blank=False)

    #produk yang dipesan
    nama_barang = models.CharField(max_length=100, null=False, blank=False)
    harga = models.DecimalField(max_digits=20, decimal_places=0,null=False, blank=False)


    class Meta:
        verbose_name = "Pesanan"
        verbose_name_plural = "Pesanans"

