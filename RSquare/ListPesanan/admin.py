from django.contrib import admin
from formpesanan.models import Pesanan
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
# Register your models here.
class ListPesananAdmin(ModelAdmin):

    model = Pesanan
    menu_label = "List Pesanan"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("id_product",'date','nama','no_wa','title','price')

modeladmin_register(ListPesananAdmin)