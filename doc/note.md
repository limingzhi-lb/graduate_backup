重写Create get_response方法来发送微信，同时判断用户身份

###触发器用来更新总价和数据库详情(check)

完成外键反向展示

订单中的商品不能选择已经完成或收货的订单()

调转货物由执行人来填写完成时间，完成时间填写完才能由领导确认

##微信通知部分添加好友或修改备注之后要刷新或重新加载，也可能是备注是数字的原因，尝试其他备注（尽量不重新登录）

## 外键的下拉选择要进行过滤 （使用formfield_for_dbfield）

### 先判断该object是哪个下拉框，然后查询数据库，设置新的queryset (check)



# 出库表单添加和更新

## 只读

### 添加

确认和完成时间等只读

###更新（创建时间一直已读）

按角色和表单状态划分，如果已确认，全只读。未确认但已完成，leader可确认，其余人全只读。未完成但当前用户是执行人，如果是leader，放开确认权限，不是则确认字段只读。如果当前用户是leader不是执行人，完成时间和确认只读，既不是leader也不是执行人全已读

## 更新表单

更新了执行人则确认和完成时间字段置空，如果确认勾选判断完成时间，没填则填写。





`create trigger update1_total_price after update on OrderFormGoods  for each row update OrderForm set total_price=(select sum(num*(select price from RawMaterial where id=OrderFormGoods.rm_name_id)) from OrderFormGoods where of_name_id=OrderForm.id);`

这一周完成了数据库结构的设计，登录，以及数据的展示功能。已开始权限控制模块的编写，预计下周完成。这周对Django的xadmin进行了深入的学习，对每一部分的功能都能正常使用。预计在下周会完成权限控制的编码并且完成对已有功能的测试。





create trigger update_stor_detail after update on OrderForm  for each row if new.is_finish=True then update StorDetail set num=(select sum(num*(select price from RawMaterial where id=OrderFormGoods.rm_name_id)) 

