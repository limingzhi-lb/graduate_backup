from xadmin.views import BaseAdminPlugin, ListAdminView, ModelFormAdminView, CreateAdminView, UpdateAdminView, DetailAdminView
import xadmin
from copy import deepcopy
from InfoManage.models import *
from InfoManage.config import Config
import datetime
from script.SendMsg import SendMsg

config = Config()


class CreateOrderFormPlugin(BaseAdminPlugin):
    create_order_form = False

    def init_request(self, *args, **kwargs):
        return bool(self.create_order_form)

    def get_form_datas(self, data):
        # print(data)
        if 'data' in data.keys():
            new_data = deepcopy(data)
            # print(type(new_data['data']))
            new_data['data']['payment_status'] = ''
            new_data['data']['is_finish'] = ''
            return new_data
        return data

    def get_read_only_fields(self, readonly_fields, *args, **kwargs):
        readonly_fields = ['delivery', 'receipt_status', 'payment_status', 'total_price', 'storage_time', 'is_finish']
        return readonly_fields


class CreateOrderFormGoodsPlugin(BaseAdminPlugin):
    order_form_goods = False
    of = OrderForm()

    def init_request(self, *args, **kwargs):
        return bool(self.order_form_goods)

    def get_form_datas(self, data):
        if 'data' in data.keys():
            # of_goods = Or
            pass
        return data


class UpdateOrderFormGoodsPlugin(BaseAdminPlugin):
    order_form_goods = False
    of_good_id = None

    def init_request(self, *args, **kwargs):
        self.of_good_id = args[0]
        return bool(self.order_form_goods)

    def get_read_only_fields(self, readonly_fields, *args, **kwargs):
        of_good = OrderFormGoods.objects.get(id=self.of_good_id)
        if of_good.of_name.is_finish:
            readonly_fields = ('rm_name', 'num', 'of_name', 'batch_number')
        return readonly_fields


class OrderFormGoodsPlugin(BaseAdminPlugin):
    order_form_goods = False
    of_good_id = None

    def init_request(self, *args, **kwargs):
        return bool(self.order_form_goods)

    def prepare_form(self, form):
        # print(form)
        return form

    def instance_forms(self, form):
        # print(form)
        return form

    def get_model_form(self, form):
        # print(form.Meta.form)
        # print(form.Meta['fields'])
        # print(form.Meta.exclude)
        # print(form.Meta.eformfield_callback)

        return form


    def get_form_layout(self, form):
        # print(type(form))
        # print(dir(form))
        # print(form.get_layout_objects)
        # print(dir(form.fields[0]))
        # print(dir(form.fields[0].fields[0]))
        # print(form.fields[0].fields[0].fields)
        return form
    # def get(self, data):
    #     print(data)
    #     return data

class UpdateOrderFormByPurchase(BaseAdminPlugin):
    update_order_form = False
    of_id = None

    def init_request(self, *args, **kwargs):
        is_purchase = self.user.groups.all()[0].name == config['purchase']
        self.of_id = args[0]
        return bool(self.update_order_form and is_purchase)

    def get_read_only_fields(self, readonly_fields, *args, **kwargs):
        # print(OrderForm.objects.get(id=self.of_id).is_finish)
        # print('*******')
        if OrderForm.objects.get(id=self.of_id).is_finish:
            readonly_fields = ['of_name', 'ven_name', 'created', 's_name', 'delivery', 'typ', 'receipt_status',
                               'payment_status', 'total_price', 'executor', 'storage_time', 'is_finish']
        elif self.user.is_leader:
            readonly_fields = ('delivery', 'receipt_status', 'storage_time', 'total_price')
            if not OrderForm.objects.get(id=self.of_id).receipt_status:
                readonly_fields = ('delivery', 'receipt_status', 'storage_time', 'total_price', 'is_finish')
        else:
            readonly_fields = ('delivery', 'receipt_status', 'storage_time', 'created', 'payment_status',
                               'total_price', 'executor', 'is_finish')
        return readonly_fields

    def get_form_datas(self, data):
        new_data = deepcopy(data)
        # print(new_data)
        if 'data' in new_data.keys() and 'is_finish' in new_data['data'].keys():
            if self.user.is_leader:
                if new_data['data']['is_finish'] == 'on':
                    new_data['data']['payment_status'] = 'on'
                    of_goods = OrderFormGoods.objects.filter(of_name=new_data['instance'].id)
                    for of_good in of_goods:
                        stor_detail = ''
                        try:
                            stor_detail = StorDetail.objects.filter(good_name=of_good.rm_name, s_name=new_data['instance'].s_name)
                        except:
                            pass
                        if stor_detail:
                            stor_detail[0].num += of_good.num
                            stor_detail[0].save()
        return new_data


class UpdateOrderFormByStor(BaseAdminPlugin):
    update_order_form = False
    of_id = None

    def init_request(self, *args, **kwargs):
        is_stor = self.user.groups.all()[0].name == config['stor']
        self.of_id = args[0]
        return bool(self.update_order_form and is_stor)

    def get_form_datas(self, data):
        new_data = deepcopy(data)
        if 'data' in new_data.keys():
            today = datetime.datetime.now().strftime('%Y/%m/%d')
            # datetime.datetime.strptime(new_data['data']['delivery_0'], '%Y/%m/%d')
            now = datetime.datetime.now().strftime("%H:%M:%S")
            if 'receipt_status' in new_data['data'].keys():
                if not new_data['data']['delivery_0'] and not new_data['data']['storage_time_0']:
                    new_data['data']['delivery_0'] = new_data['data']['storage_time_0'] = today
                    new_data['data']['delivery_1'] = new_data['data']['storage_time_1'] = now
                elif not new_data['data']['delivery_0']:
                    new_data['data']['delivery_0'] = new_data['data']['storage_time_0']
                    new_data['data']['delivery_1'] = new_data['data']['storage_time_1']
                elif not new_data['data']['storage_time_0']:
                    new_data['data']['storage_time_0'] = new_data['data']['delivery_0']
                    new_data['data']['storage_time_1'] = new_data['data']['delivery_1']
            elif 'delivery_0' in new_data['data'].keys():
                if new_data['data']['delivery_0'] or new_data['data']['storage_time_0']:
                    new_data['data']['receipt_status'] = 'on'
                    if not new_data['data']['delivery_0']:
                        new_data['data']['delivery_0'] = new_data['data']['storage_time_0']
                        new_data['data']['delivery_1'] = new_data['data']['storage_time_1']
                    elif not new_data['data']['storage_time_0']:
                        new_data['data']['storage_time_0'] = new_data['data']['delivery_0']
                        new_data['data']['storage_time_1'] = new_data['data']['delivery_1']
                delivery = datetime.datetime.strptime(new_data['data']['delivery_0'], '%Y/%m/%d')
                storage = datetime.datetime.strptime(new_data['data']['storage_time_0'], '%Y/%m/%d')

                today_ = datetime.datetime.strptime(today, '%Y/%m/%d')
                now_ = datetime.datetime.strptime(now, "%H:%M:%S")
                if delivery >= today_:
                    new_data['data']['delivery_0'] = today
                    if datetime.datetime.strptime(new_data['data']['delivery_1'], "%H:%M") > now_:
                        new_data['data']['delivery_1'] = now
                if storage >= today_:
                    new_data['data']['storage_time_0'] = today
                    if datetime.datetime.strptime(new_data['data']['storage_time_1'], "%H:%M") > now_:
                        new_data['data']['dstorage_time_1'] = now
                group = 'purchase'
                msg = u'你有一个订单需要确认，请及时处理。'
            # SendMsg(group, msg)
        return new_data

    def get_read_only_fields(self, readonly_fields, *args, **kwargs):
        if OrderForm.objects.get(id=self.of_id).is_finish:
            readonly_fields = ['of_name', 'ven_name', 'created', 's_name', 'delivery', 'typ', 'receipt_status',
                               'payment_status', 'total_price', 'executor', 'storage_time', 'is_finish']
        else:
            readonly_fields = ('of_name', 'ven_name', 'created', 's_name', 'typ', 'payment_status',
                               'total_price', 'executor', 'is_finish')
        return readonly_fields


class ViewOrderFormDetail(BaseAdminPlugin):
    view_order_form_detail = False

    def init_request(self, *args, **kwargs):
        return bool(self.view_order_form_detail)


class test(BaseAdminPlugin):
    view_order_form_detail = True

    def init_request(self, *args, **kwargs):
        return bool(self.view_order_form_detail)

    def get_readonly_fields(self, readonly_fields):
        # print(self.re)
        # print(OrderForm.objects.get(id=self.of_id).is_finish)
        # readonly_fields = []
        if OrderForm.objects.get(id=self.of_id).is_finish:
            # print(type(data.Meta.exclude))
            # print(readonly_fields)
            # print('**&&&&&')
            readonly_fields = ['of_name', 'ven_name', 'created', 's_name', 'delivery', 'typ', 'receipt_status',
                               'payment_status', 'total_price', 'executor', 'storage_time', 'is_finish']
        return readonly_fields

# class


xadmin.site.register_plugin(CreateOrderFormPlugin, CreateAdminView)
xadmin.site.register_plugin(CreateOrderFormGoodsPlugin, CreateAdminView)
xadmin.site.register_plugin(UpdateOrderFormByStor, UpdateAdminView)
xadmin.site.register_plugin(UpdateOrderFormByPurchase, UpdateAdminView)
xadmin.site.register_plugin(UpdateOrderFormGoodsPlugin, UpdateAdminView)
xadmin.site.register_plugin(OrderFormGoodsPlugin, ModelFormAdminView)
# xadmin.site.register_plugin(ViewOrderFormDetail, DetailAdminView)
# xadmin.site.register_plugin(test, ModelFormAdminView)

