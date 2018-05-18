from xadmin.views import BaseAdminPlugin, ListAdminView, ModelFormAdminView, CreateAdminView, UpdateAdminView, DetailAdminView
import xadmin
from copy import deepcopy
from InfoManage.models import *
from InfoManage.config import Config
from django.forms.models import ModelChoiceField
from django.contrib.auth.models import Group
from users.models import User
import datetime
config = Config()


class CreateSaleFormPlugin(BaseAdminPlugin):
    sale_form = False

    def init_request(self, *args, **kwargs):
        return bool(self.sale_form)

    def formfield_for_dbfield(self, data, *args, **kwargs):
        if isinstance(data, ModelChoiceField):
            queryset = data._get_queryset()
            if isinstance(queryset[0], User):
                group = Group.objects.get(name=config['sale'])
                queryset = group.user_set.all()
                data._set_queryset(queryset)
        return data

    def get_read_only_fields(self, readonly_fields, *args, **kwargs):
        readonly_fields = ('price', 'deliver_date', 'state', 'check', 'out_stor_date')
        return readonly_fields

    def get_form_datas(self, data):
        new_data = deepcopy(data)
        if 'data' in new_data.keys():
            pass
        return new_data


class UpdateSaleFormPlugin(BaseAdminPlugin):
    sale_form = False
    sf_id = None

    def init_request(self, *args, **kwargs):
        self.sf_id = args[0]
        return bool(self.sale_form)

    def formfield_for_dbfield(self, data, *args, **kwargs):
        if isinstance(data, ModelChoiceField):
            queryset = data._get_queryset()
            if isinstance(queryset[0], User):
                group = Group.objects.get(name=config['sale'])
                queryset = group.user_set.all()
                data._set_queryset(queryset)
        return data

    def get_read_only_fields(self, readonly_fields, *args, **kwargs):
        readonly_fields = ('sf_name', 'staff_name', 'c_name', 'price', 'created', 'deliver_date',
                           'state', 'check', 'out_stor_date')
        sf = SaleForm.objects.get(id=self.sf_id)
        if sf.check:
            readonly_fields = ('sf_name', 'staff_name', 'c_name', 'price', 'created', 'deliver_date',
                     'state', 'check', 'out_stor_date')
        elif sf.deliver_date:
            if self.user.is_leader and self.user.groups.all()[0].name == config['sale']:
                readonly_fields = ('sf_name', 'staff_name', 'c_name', 'price', 'created', 'deliver_date',
                                   'state','out_stor_date')
        elif sf.state:
            readonly_fields = ('sf_name', 'staff_name', 'c_name', 'price', 'created', 'deliver_date',
                     'state', 'check', 'out_stor_date')
            if self.user.id == sf.staff_name.id:
                readonly_fields = ('sf_name', 'staff_name', 'c_name', 'price', 'created',
             'state', 'check', 'out_stor_date')
                if self.user.is_leader:
                    readonly_fields = ('sf_name', 'staff_name', 'c_name', 'price', 'created',
                                   'state', 'out_stor_date')
        elif (self.user.is_leader or self.user.id == sf.state.id) and self.user.groups.all()[0].name == config['sale']:
            readonly_fields = ('price', 'created', 'deliver_date',
                               'state', 'check', 'out_stor_date')
        elif self.user.groups.all()[0].name == config['stor'] and not sf.state:
            readonly_fields = ('sf_name', 'staff_name', 'c_name', 'price', 'created', 'deliver_date',
                               'check')
        return readonly_fields

    def get_form_datas(self, data):
        new_data = deepcopy(data)
        if 'data' in new_data.keys():
            today = datetime.datetime.now().strftime('%Y/%m/%d')
            now = datetime.datetime.now().strftime("%H:%M:%S")
            if 'state' in new_data['data'].keys():
                if new_data['data']['state']:
                    if 'out_stor_date_0' not in new_data['data'].keys():
                        new_data['data']['out_stor_date_0'] = today
                        new_data['data']['out_stor_date_1'] = now
                    elif not new_data['data']['out_stor_date_0']:
                        new_data['data']['out_stor_date_0'] = today
                        new_data['data']['out_stor_date_1'] = now
            if 'out_stor_date_0' in new_data['data'].keys():
                if new_data['data']['out_stor_date_0']:
                    new_data['data']['state'] = 'on'
        return new_data


class CreateSaleFormProductPlugin(BaseAdminPlugin):
    sale_form_product = False

    def init_request(self, *args, **kwargs):
        return bool(self.sale_form_product)

    def formfield_for_dbfield(self, data, *args, **kwargs):
        if isinstance(data, ModelChoiceField):
            queryset = data._get_queryset()
            if isinstance(queryset[0], SaleForm):
                group = SaleForm.objects.filter(check=False, staff_name=self.user.id)
                queryset = group.all()
                data._set_queryset(queryset)
        return data

    def get_read_only_fields(self, readonly_fields, *args, **kwargs):
        readonly_fields = ('price',)
        return readonly_fields

    def get_form_datas(self, data):
        new_data = deepcopy(data)
        print(new_data)
        stordetails = StorDetail.objects.all()
        if 'data' in new_data.keys():
            product = Product.objects.get(id=data['data']['pro_name'])
            print(product)

            stordetail = StorDetail.objects.filter(good_name=product.pro_name)
            if int(new_data['data']['num']) > stordetail[0].num:
                new_data['data']['num'] = str(stordetail[0].num)
            new_data['data']['price'] = str(product.price*int(new_data['data']['num']))
            sale_form = SaleForm.objects.get(id=new_data['data']['sf_name'])
            if sale_form.price:
                sale_form.price += product.price*int(new_data['data']['num'])
            else:
                sale_form.price = product.price*int(new_data['data']['num'])
            sale_form.save()

        return new_data


class UpdateSaleFormProductPlugin(BaseAdminPlugin):
    sale_form_product = False
    sfp_id = None

    def init_request(self, *args, **kwargs):
        self.sfp_id = args[0]
        return bool(self.sale_form_product)

    def formfield_for_dbfield(self, data, *args, **kwargs):
        if isinstance(data, ModelChoiceField):
            queryset = data._get_queryset()
            if isinstance(queryset[0], SaleForm):
                group = SaleForm.objects.filter(check=False, staff_name=self.user.id)
                queryset = group.all()
                data._set_queryset(queryset)
        return data

    def get_read_only_fields(self, readonly_fields, *args, **kwargs):
        readonly_fields = ('price',)
        sf = SaleFormProduct.objects.get(id=self.sfp_id)
        if sf.sf_name.check:
            readonly_fields = ('sf_name', 'pro_name', 'num')
        return readonly_fields

    def get_form_datas(self, data):
        new_data = deepcopy(data)
        # print(new_data)
        if 'data' in new_data.keys():
            product = Product.objects.get(id=data['data']['pro_name'])
            stordetail = StorDetail.objects.filter(good_name=product.pro_name)
            if int(new_data['data']['num']) > stordetail[0].num:
                new_data['data']['num'] = str(stordetail[0].num)
        # print(new_data)
        return new_data



xadmin.site.register_plugin(CreateSaleFormPlugin, CreateAdminView)
xadmin.site.register_plugin(CreateSaleFormProductPlugin, CreateAdminView)
xadmin.site.register_plugin(UpdateSaleFormPlugin, UpdateAdminView)
xadmin.site.register_plugin(UpdateSaleFormProductPlugin, UpdateAdminView)
