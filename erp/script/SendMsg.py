import itchat
from users.models import User
from InfoManage.config import Config
from django.contrib.auth.models import Group
config = Config()

class SendMsg(object):
    def __init__(self, group, msg):
        group = Group.objects.get(name=group)
        self.msg = msg
        # self.user = User.objects.get(is_leader=True, group=group.id)
        # print(self.user)
        user = group.user_set.all()
        self.user = user.get(is_leader=True)
        print(self.user)
        self.user = 'Lady'

    def send(self):
        # print('*****')
        users = itchat.search_friends(name=self.user)
        # print(users)
        userName = users[0]['UserName']
        itchat.send(self.msg, toUserName=userName)
        # print('#####')


# group = config['purchase']
# msg = u'你有一个订单需要确认，请及时处理。'
# send = SendMsg(group, msg)
# send.send()
