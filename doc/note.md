重写Create get_response方法来发送微信，同时判断用户身份

###触发器用来更新总价和数据库详情(check)

完成外键反向展示

订单中的商品不能选择已经完成或收货的订单()

调转货物由执行人来填写完成时间，完成时间填写完才能由领导确认

##微信通知部分添加好友或修改备注之后要刷新或重新加载，也可能是备注是数字的原因，尝试其他备注（尽量不重新登录）

## 外键的下拉选择要进行过滤





`create trigger update1_total_price after update on OrderFormGoods  for each row update OrderForm set total_price=(select sum(num*(select price from RawMaterial where id=OrderFormGoods.rm_name_id)) from OrderFormGoods where of_name_id=OrderForm.id);`

这一周完成了数据库结构的设计，登录，以及数据的展示功能。已开始权限控制模块的编写，预计下周完成。这周对Django的xadmin进行了深入的学习，对每一部分的功能都能正常使用。预计在下周会完成权限控制的编码并且完成对已有功能的测试。





create trigger update_stor_detail after update on OrderForm  for each row if new.is_finish=True then update StorDetail set num=(select sum(num*(select price from RawMaterial where id=OrderFormGoods.rm_name_id)) 



{'instance': <OrderForm: 18.4.28采购原材料1-3>, 'data': <QueryDict: {'csrfmiddlewaretoken': ['j41BHVSuHBpeeuHtwUutLTrqBPNN9JKO0zpeHj5qmLabMzjCxLpnxYuDYrm5PZe8', 'j41BHVSuHBpeeuHtwUutLTrqBPNN9JKO0zqmLabMzjCxLpnxYuDYrm5PZe8'], 'delivery_0': ['2018/04/29'], 'delivery_1': ['14:33'], 'storage_time_0': ['2018/04/29'], 'storage_time_1': ['14:31'], '_save': ['']}>, 'files': <MultiValueDict: {}>}
9