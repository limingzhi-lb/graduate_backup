import xadmin
from xadmin import views
from .models import *
from django.contrib import admin
from .config import Config
'''
    添加配置文件，自己定义读取user_group的脚本，获取信息
'''


class BaseSetting(object):

    enable_themes = True
    use_bootswatch = True


class VenderAdmin(object):
    say_hello = True
    list_display = ['ven_name', 'addr', 'tel', 'created', 'updated', 'rm_name']
    search_fields = ['ven_name', 'addr', 'tel', 'created', 'updated', 'rm_name']
    list_filter = ['ven_name', 'addr', 'tel', 'created', 'updated', 'rm_name']
    read_only_fields = ('ven_name', 'addr')
    list_per_page = 5
    filter_horizontal = ('rm_name',)


class RawMaterialAdmin(object):
    say_hello = False
    used = False
    # edit = True
    list_display = ['rm_name', 'price', 'classification', 'minimum_inventory', 'created', 'updated']
    search_fields = ['rm_name', 'price', 'classification', 'minimum_inventory', 'created', 'updated']
    list_filter = ['rm_name', 'price', 'classification', 'minimum_inventory', 'created', 'updated']
    # readonly_fields = ('price',)
    list_per_page = 5


class StorDetailInline(object):
    model = StorDetail
    extra = 0


class StorAdmin(object):
    list_display = ['s_name', 'valid']
    search_fields = ['s_name', 'valid']
    list_filter = ['s_name', 'valid']
    list_per_page = 5
    # inlines = [StorDetailInline, ]


class StorDetailAdmin(object):
    list_display = ['good_name', 'num']
    search_fields = ['good_name', 'num']
    list_filter = ['good_name', 'num']
    list_per_page = 5


class OrderFormAdmin(object):
    create_order_form = True
    update_order_form = True
    view_order_form_detail = True
    order_form = True
    list_display = ['of_name', 'ven_name', 'created', 'delivery', 'typ', 'receipt_status', 'payment_status',
                    'total_price', 'executor', 'storage_time', 'is_finish']
    search_fields = ['of_name', 'ven_name', 'created', 'delivery', 'typ', 'receipt_status', 'payment_status',
                     'total_price', 'executor', 'storage_time', 'is_finish']
    list_filter = ['of_name', 'ven_name', 'created', 'delivery', 'typ', 'receipt_status', 'payment_status',
                   'total_price', 'executor', 'storage_time', 'is_finish']
    list_per_page = 5
    # inlines = [OrderFormGoodsInline, ]

    # def rm_name(self, obj):
    #     return
    # def get_readonly_fields(self):
    #     # user_id = self.user.id
    #     group = Config()
    #     print(self.user.groups.all()[0].name)
    #     if self.user.groups.all()[0].name == group['stor']:
    #         self.readonly_fields = ('of_name', 'ven_name', 'created', 's_name', 'typ', 'payment_status',
    #                                 'total_price', 'executor', 'is_finish')
    #         return self.readonly_fields
    #     elif self.user.groups.all()[0].name == group['purchase']:
    #         if not self.user.is_leader:
    #             self.readonly_fields = ('delivery', 'receipt_status', 'payment_status', 'executor',
    #                                     'storage_time', 'is_finish')
    #         else:
    #             self.readonly_fields = ('delivery', 'receipt_status', 'storage_time')
    #         return self.readonly_fields
    #     return self.readonly_fields


class OrderFormGoodsAdmin(object):
    order_form_goods = True
    list_display = ['rm_name', 'num', 'of_name']
    search_fields = ['rm_name', 'num', 'of_name']
    list_filter = ['rm_name', 'num', 'of_name']
    list_per_page = 5

    # def get_form(self, request, obj=None, **kwargs):
    #     return super(OrderFormGoodsAdmin, self).get_form(request, obj, **kwargs)
    #
    # def get_fieldsets(self, request, obj=None):
    #     """
    #     Hook for specifying fieldsets.
    #     """
    #     if self.fieldsets:
    #         return self.fieldsets
    #     return [(None, {'fields': self.get_fields(request, obj)})]


# class SwapFormDetailInline(object):
#     model = SwapFormDetail
#     extra = 0

class SwapFormAdmin(object):
    swap_form = True
    list_display = ['sf_name', 'staff_name', 'before_s_id', 'after_s_id', 'created', 'finished', 'check']
    search_fields = ['sf_name', 'staff_name', 'before_s_id', 'after_s_id', 'created', 'finished', 'check']
    list_filter = ['sf_name', 'staff_name', 'before_s_id', 'after_s_id', 'created', 'finished', 'check']
    list_per_page = 5


class SwapFormDetailAdmin(object):
    swap_form_detail = True
    swap_form = True
    list_display = ['good_name', 'num', 'sf_name']
    search_fields = ['good_name', 'num', 'sf_name']
    list_filter = ['good_name', 'num', 'sf_name']
    list_per_page = 5


class OutStorDetailAdmin(object):
    out_stor_detail = True
    list_display = ['good_name', 'num', 'osf_name']
    search_fields = ['good_name', 'num', 'osf_name']
    list_filter = ['good_name', 'num', 'osf_name']
    list_per_page = 5



# class OutStorDetailInline(object):
#     model = OutStorDetail
#     extra = 1


class OutStoreFormAdmin(object):
    create_out_stor = True
    update_out_stor = True
    list_display = ['osf_name', 'created', 'staff_id', 'check', 'note', 'finished']
    search_fields = ['osf_name', 'created', 'staff_id', 'check', 'note', 'finished']
    list_filter = ['osf_name', 'created', 'staff_id', 'check', 'note', 'finished']
    list_per_page = 5
    # inlines = [OutStorDetailInline, ]


class ProductAdmin(object):
    list_display = ['pro_name', 'price']
    search_fields = ['pro_name', 'price']
    list_filter = ['pro_name', 'price']
    list_per_page = 5


class HalfproductAdmin(object):
    list_display = ['hp_name']
    search_fields = ['hp_name']
    list_filter = ['hp_name']
    list_per_page = 5


class MeterialAdmin(object):
    list_display = ['m_id', 'name', 'num', 'product', 'hp_name']
    search_fields = ['m_id', 'name', 'num', 'product', 'hp_name']
    list_filter = ['m_id', 'name', 'num', 'product', 'hp_name']
    list_per_page = 5


class AssembliLineAdmin(object):
    list_display = ['ass_name']
    search_fields = ['ass_name']
    list_filter = ['ass_name']
    list_per_page = 5


class ProduceFormAdmin(object):
    list_display = ['pf_name', 'pro_name', 'pro_num', 'hpro_name', 'hpro_num', 'created',
                    'assembly_line', 'actual_num', 'is_instor', 'note', 'is_finish', 's_name', 'qualified_rate']
    search_fields = ['pf_name', 'pro_name', 'pro_num', 'hpro_name', 'hpro_num', 'created',
                     'assembly_line', 'actual_num', 'is_instor', 'note', 'is_finish', 's_name', 'qualified_rate']
    list_filter = ['pf_name', 'pro_name', 'pro_num', 'hpro_name', 'hpro_num', 'created',
                   'assembly_line', 'actual_num', 'is_instor', 'note', 'is_finish', 's_name', 'qualified_rate']
    list_per_page = 5


class WasteFormAdmin(object):
    list_display = ['name', 'num', 'pf_name']
    search_fields = ['name', 'num', 'pf_name']
    list_filter = ['name', 'num', 'pf_name']
    list_per_page = 5


class CustomerAdmin(object):
    list_display = ['c_name', 'tel', 'addr']
    search_fields = ['c_name', 'tel', 'addr']
    list_filter = ['c_name', 'tel', 'addr']
    list_per_page = 5


class SaleFormProductInline(object):
    model = SaleFormProduct
    extra = 0


class SaleFormAdmin(object):
    list_display = ['sf_name', 'staff_name', 'c_name', 'price', 'created', 'deliver_date',
                    's_name', 'state', 'check', 'out_stor_date']
    search_fields = ['sf_name', 'staff_name', 'c_name', 'price', 'created', 'deliver_date',
                     's_name', 'state', 'check', 'out_stor_date']
    list_filter = ['sf_name', 'staff_name', 'c_name', 'price', 'created', 'deliver_date',
                   's_name', 'state', 'check', 'out_stor_date']
    list_per_page = 5
    # inlines = [SaleFormProductInline, ]


class SaleFormProductAdmin(object):
    list_display = ['sf_name', 'pro_name', 'num', 'price']
    search_fields = ['sf_name', 'pro_name', 'num', 'price']
    list_filter = ['sf_name', 'pro_name', 'num', 'price']
    list_per_page = 5


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
xadmin.site.register(OrderFormGoods, OrderFormGoodsAdmin)
# xadmin.site.register(Stor, StorAdmin)
# xadmin.site.register(SwapForm, SwapFormAdmin)
# xadmin.site.register(SwapFormDetail, SwapFormDetailAdmin)
xadmin.site.register(OutStorForm, OutStoreFormAdmin)
xadmin.site.register(OutStorDetail, OutStorDetailAdmin)
xadmin.site.register(Product, ProductAdmin)
xadmin.site.register(HalfProduct, HalfproductAdmin)
xadmin.site.register(ProduceForm, ProduceFormAdmin)
xadmin.site.register(WasteForm, WasteFormAdmin)
xadmin.site.register(Customer, CustomerAdmin)
xadmin.site.register(SaleForm, SaleFormAdmin)
xadmin.site.register(SaleFormProduct, SaleFormProductAdmin)
xadmin.site.register(StorDetail, StorDetailAdmin)


