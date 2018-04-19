import xadmin
from xadmin import views
from .models import *


class BaseSetting(object):

    enable_themes = True
    use_bootswatch = True


class VenderAdmin(object):
    say_hello = True
    list_display = ['ven_name', 'addr', 'tel', 'created', 'updated', 'rm_name']
    search_fields = ['ven_name', 'addr', 'tel', 'created', 'updated', 'rm_name']
    list_filter = ['ven_name', 'addr', 'tel', 'created', 'updated', 'rm_name']
    read_only_fields = ('ven_name', 'addr')


class RawMaterialAdmin(object):
    say_hello = True
    used = True
    list_display = ['rm_name', 'price', 'classification', 'minimum_inventory', 'batch_number', 'created', 'updated']
    search_fields = ['rm_name', 'price', 'classification', 'minimum_inventory', 'batch_number', 'created', 'updated']
    list_filter = ['rm_name', 'price', 'classification', 'minimum_inventory', 'batch_number', 'created', 'updated']
    read_only_fields = ['price']


class OrderFormAdmin(object):
    list_display = ['of_id', 'ven_id', 'created', 's_id', 'delivery', 'typ', 'receipt_status', 'payment_status',
                    'total_price', 'executor', 'storage_time', 'is_finish']


class GlobalSetting(object):
    site_title = 'ERP'
    site_footer = '我的公司'
    menu_style = "accordion"
    global_models_icon = {
        Vender: "glyphicon glyphicon-user", RawMaterial: "fa fa-cloud"
    }





xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(Vender, VenderAdmin)
xadmin.site.register(RawMaterial, RawMaterialAdmin)
xadmin.site.register(OrderForm, OrderFormAdmin)
