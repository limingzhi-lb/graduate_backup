from django.contrib.postgres.fields import JSONField
from django.db import models
import json


# class JSONField(models.TextField):
#     __metaclass__ = models.SubfieldBase
#     description = "Json"
#
#     def to_python(self, value):
#         v = models.TextField.to_python(self, value)
#         try:
#             return json.loads(v)['v']
#         except:
#             pass
#         return v
#
#     def get_prep_value(self, value):
#         return json.dumps({'v': value})


class Vender(models.Model):
    __name__ = 'Vender'
    ven_name = models.CharField(max_length=24, primary_key=True)
    addr = models.CharField(max_length=24)
    tel = models.CharField(max_length=12)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    rm_name = JSONField()


class RawMaterial(models.Model):
    __name__ = 'RawMaterial'
    rm_name = models.CharField(max_length=24, primary_key=True)
    price = models.FloatField()
    classification = models.CharField(max_length=8)
    minimum_inventory = models.IntegerField()
    batch_number = models.CharField(max_length=8)
    created = models.DateTimeField()
    updated = models.DateTimeField()


class OrderForm(models.Model):
    __name__ = 'OrderForm'
    of_id = models.IntegerField(primary_key=True)
    ven_id = models.IntegerField()
    created = models.DateTimeField()
    s_id = models.IntegerField(default=0)
    delivery = models.DateTimeField()
    typ = models.BooleanField(default=1)
    receipt_status = models.BooleanField(default=0)
    payment_status = models.BooleanField(default=0)
    total_price = models.FloatField()
    executor = models.IntegerField()
    storage_time = models.DateTimeField()
    is_finish = models.BooleanField(default=0)


class OrderFormGoods(models.Model):
    __name__ = 'OrderFormGoods'
    rm_name = models.CharField(max_length=24)
    of_id = models.IntegerField(primary_key=True)
    num = models.IntegerField()

    class Meta:
        unique_together = ('rm_name', 'of_id')


class Stor(models.Model):
    __name__ = 'Stor'
    s_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=12)
    valid = models.BooleanField(default=1)


class SwapForm(models.Model):
    __name__ = 'SwapForm'
    sf_id = models.IntegerField(primary_key=True)
    staff_id = models.IntegerField()
    before_s_id = models.IntegerField()
    after_s_id = models.IntegerField()
    created = models.DateTimeField()
    finished = models.DateTimeField()
    check = models.BooleanField(default=0)
    sf_detail_id = models.IntegerField()


class SwapFormDetail(models.Model):
    __name__ = 'SwapFormDetail'
    sf_detail_id = models.IntegerField(primary_key=True)
    good_name = models.CharField(max_length=24)
    num = models.IntegerField()
    batch_number = models.CharField(max_length=8)
    sf_id = models.IntegerField()


class OutStorForm(models.Model):
    __name__ = 'OutStorForm'
    osf_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()
    after_s_id = models.DateTimeField()
    staff_id = models.IntegerField()
    check = models.BooleanField(default=0)
    note = models.CharField(max_length=64)
    finished = models.DateTimeField()
    osd_id = JSONField()


class OutStorDetail(models.Model):
    __name__ = 'OutStorDetail'
    osd_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=24)
    num = models.IntegerField()
    batch_number = models.CharField(max_length=8)
    osf_id = models.IntegerField()


class Product(models.Model):
    __name__ = 'Product'
    pro_name = models.CharField(max_length=8,primary_key=True)
    rm = JSONField()
    hp = JSONField()
    price = models.FloatField()


class HalfProduct(models.Model):
    __name__ = 'HalfProduct'
    hp_name = models.CharField(max_length=8,primary_key=True)
    rm = JSONField()
    hp = JSONField()


class ProduceForm(models.Model):
    __name__ = 'ProduceForm'
    pf_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=8)
    num = models.IntegerField()
    created = models.DateTimeField()
    assembly_line = models.IntegerField()
    actual_num = models.IntegerField()
    is_instor = models.BooleanField(default=0)
    note = models.TextField()
    is_finish = models.BooleanField(default=0)
    s_id = models.IntegerField()
    qualified_rate = models.FloatField()


class WasteForm(models.Model):
    __name__ = 'WasteForm'
    name = models.CharField(max_length=8)
    num = models.IntegerField()
    pf_id = models.IntegerField()

    class Meta:
        unique_together = ('name', 'pf_id')


class Customer(models.Model):
    __name__ = 'Customer'
    c_name = models.CharField(max_length=24, primary_key=True)
    tel = models.CharField(max_length=12)
    addr = models.CharField(max_length=32)


class SaleForm(models.Model):
    __name__ = 'SaleForm'
    sf_id = models.IntegerField(primary_key=True)
    staff_id = models.IntegerField()
    c_id = models.IntegerField()
    price = models.IntegerField()
    created = models.DateTimeField()
    deliver_date = models.DateTimeField()
    s_id = models.IntegerField()
    state = models.BooleanField(default=0)
    pro_name = JSONField()
    check = models.BooleanField(default=0)
    out_stor_date = models.DateTimeField()


class SaleFormProduct(models.Model):
    __name__ = 'SaleFormProduct'
    sf_id = models.IntegerField(primary_key=True)
    pro_name = models.CharField(max_length=8)
    num = models.IntegerField()
    price = models.IntegerField()
    class Meta:
        unique_together = ('sf_id', 'pro_name')


class StorDetail(models.Model):
    __name__ = 'StorDetail'
    name = models.CharField(max_length=12, primary_key=True)
    num = models.IntegerField()
    s_id = models.IntegerField()

    class Meta:
        unique_together = ('name', 's_id')

