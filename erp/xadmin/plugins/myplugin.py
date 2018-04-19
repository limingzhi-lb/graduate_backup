from xadmin.views import BaseAdminPlugin, ListAdminView, CreateAdminView
import xadmin


class FirstPlugin(BaseAdminPlugin):
    say_hello = False

    # 初始化方法根据 ``say_hello`` 属性值返回
    def init_request(self, *args, **kwargs):
        return bool(self.say_hello)


class ListPlugin(BaseAdminPlugin):
    used = False
    def init_request(self, *args, **kwargs):
        return bool(self.used)
    # def get_list_display(self, list_display):
        # if self.used:
        #     list_display = []
            # self.admin_view.over_view = self.over_view
        # return list_display
    def get_context(self, context):
        if self.used:
            print(context)
            return context
        # pass
    # def get_list_queryset(self, result_list):
    #     if self.used:
    #         print(result_list)

xadmin.site.register_plugin(FirstPlugin, CreateAdminView)
xadmin.site.register_plugin(ListPlugin, ListAdminView)
