from django.contrib import admin
from formpesanan.models import Pesanan
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from wagtail.contrib.modeladmin.helpers import PermissionHelper
# Register your models here.

class ValidationPermissionHelper(PermissionHelper):
    def user_can_list(self, user):
        return True
    def user_can_create(self, user):
        return False
    def user_can_edit_obj(self, user, obj):
        return False
class ListPesananAdmin(ModelAdmin):

    model = Pesanan
    menu_label = "List Pesanan"
    permission_helper_class = ValidationPermissionHelper
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("id_product",'date','nama','no_wa','title','price','alamat','catatan')

modeladmin_register(ListPesananAdmin)