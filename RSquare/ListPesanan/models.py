"""List Pesanan"""

from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page

from django.shortcuts import render
from formpesanan.models import Pesanan


# Create your models here.
class ListPesananPage(Page):

    #content

    #pemesan


    #produk yang dipesan


    class Meta:
        verbose_name = "Pesanan"
        verbose_name_plural = "Pesanans"
