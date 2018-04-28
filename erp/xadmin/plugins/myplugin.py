from xadmin.views import BaseAdminPlugin, ListAdminView, CreateAdminView, UpdateAdminView
import xadmin
from copy import deepcopy


class FirstPlugin(BaseAdminPlugin):
    say_hello = False

    # 初始化方法根据 ``say_hello`` 属性值返回
    def init_request(self, *args, **kwargs):
        return bool(self.say_hello)


class CreateOrderFormPlugin(BaseAdminPlugin):
    use = False

    def init_request(self, *args, **kwargs):
        return bool(self.use)

    def get_form_datas(self, data):
        print(data)
        if 'data' in data.keys():
            new_data = deepcopy(data)
            print(type(new_data['data']))
            new_data['data']['payment_status'] = ''
            new_data['data']['is_finish'] = ''
            return new_data
        return data


xadmin.site.register_plugin(FirstPlugin, CreateAdminView)
xadmin.site.register_plugin(CreateOrderFormPlugin, CreateAdminView)

