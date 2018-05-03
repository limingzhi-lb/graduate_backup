from xadmin.views import BaseAdminPlugin, ListAdminView, ModelFormAdminView, CreateAdminView, UpdateAdminView, DetailAdminView
import xadmin
from copy import deepcopy
from InfoManage.models import *
from InfoManage.config import Config
import datetime


class CreateSwapForm(BaseAdminPlugin):
    swap_form = False

    def init_request(self, *args, **kwargs):
        return bool(self.swap_form)

    def get_read_only_fields(self, readonly_fields, *args, **kwargs):
        readonly_fields = ('finished', 'check')
        return readonly_fields

class SwapFormDetail(BaseAdminPlugin):
    swap_form_detail = False

    def init_request(self, *args, **kwargs):
        return bool(self.swap_form_detail)

    def get_form_datas(self, data):
        new_data = deepcopy(data)
        if 'data' in new_data:
            sf = SwapForm.objects.get(id=new_data['data']['sf_name'])
            stor_detail = StorDetail.objects.get(good_name=new_data['instance'].good_name, s_name=sf.before_s_id)
            if stor_detail.num < int(new_data['data']['num']):
                new_data['data']['num'] = str(stor_detail.num)
        return new_data











xadmin.site.register_plugin(CreateSwapForm, CreateAdminView)
xadmin.site.register_plugin(SwapFormDetail, CreateAdminView)
xadmin.site.register_plugin(SwapFormDetail, UpdateAdminView)
