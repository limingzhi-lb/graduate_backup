# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-23 15:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AssemblyLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ass_name', models.CharField(max_length=24, verbose_name='名称')),
            ],
            options={
                'verbose_name': '生产线',
                'verbose_name_plural': '生产线',
                'db_table': 'AssemblyLine',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=24, verbose_name='客户名')),
                ('tel', models.CharField(max_length=12, verbose_name='电话')),
                ('addr', models.CharField(max_length=32, verbose_name='地址')),
            ],
            options={
                'verbose_name': '客户',
                'verbose_name_plural': '客户',
                'db_table': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='HalfProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hp_name', models.CharField(max_length=8, verbose_name='半成品名')),
            ],
            options={
                'verbose_name': '半成品',
                'verbose_name_plural': '半成品',
                'db_table': 'HalfProduct',
            },
        ),
        migrations.CreateModel(
            name='Meterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='数量')),
                ('hp_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meterial_hp_name', to='InfoManage.HalfProduct', verbose_name='半成品')),
            ],
            options={
                'verbose_name': '零部件',
                'verbose_name_plural': '零部件',
                'db_table': 'Meterial',
            },
        ),
        migrations.CreateModel(
            name='OrderForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('of_name', models.CharField(max_length=32, verbose_name='订单名称')),
                ('created', models.DateTimeField(verbose_name='创建时间')),
                ('delivery', models.DateTimeField(verbose_name='交货时间')),
                ('typ', models.BooleanField(default=1, verbose_name='订单类型')),
                ('receipt_status', models.BooleanField(default=0, verbose_name='是否收货')),
                ('payment_status', models.BooleanField(default=0, verbose_name='支付状态')),
                ('total_price', models.FloatField(verbose_name='总价')),
                ('storage_time', models.DateTimeField(verbose_name='入库时间')),
                ('is_finish', models.BooleanField(default=0, verbose_name='是否完成')),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_form_username', to=settings.AUTH_USER_MODEL, verbose_name='执行人')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
                'db_table': 'OrderForm',
            },
        ),
        migrations.CreateModel(
            name='OrderFormGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='数量')),
                ('batch_number', models.CharField(max_length=8, verbose_name='批次号')),
                ('of_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_form_goods_of_name', to='InfoManage.OrderForm', verbose_name='订单')),
            ],
            options={
                'verbose_name': '订单中商品',
                'verbose_name_plural': '订单中商品',
                'db_table': 'OrderFormGoods',
            },
        ),
        migrations.CreateModel(
            name='OutStorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='数量')),
            ],
            options={
                'verbose_name': '出库货物',
                'verbose_name_plural': '出库货物',
                'db_table': 'OutStorDetail',
            },
        ),
        migrations.CreateModel(
            name='OutStorForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osf_name', models.CharField(max_length=32, verbose_name='表名')),
                ('created', models.DateTimeField(verbose_name='创建时间')),
                ('check', models.BooleanField(default=0, verbose_name='是否确认')),
                ('note', models.CharField(max_length=64, verbose_name='备注')),
                ('finished', models.DateTimeField(verbose_name='完成时间')),
            ],
            options={
                'verbose_name': '出库表',
                'verbose_name_plural': '出库表',
                'db_table': 'OutStorForm',
            },
        ),
        migrations.CreateModel(
            name='ProduceForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_name', models.CharField(max_length=32, verbose_name='表名')),
                ('pro_num', models.IntegerField(verbose_name='成品数量')),
                ('hpro_num', models.IntegerField(verbose_name='半成品数量')),
                ('created', models.DateTimeField(verbose_name='创建时间')),
                ('actual_num', models.IntegerField(verbose_name='实际数量')),
                ('is_instor', models.BooleanField(default=0, verbose_name='是否入库')),
                ('note', models.TextField(verbose_name='备注')),
                ('is_finish', models.BooleanField(default=0, verbose_name='是否完成')),
                ('qualified_rate', models.FloatField(verbose_name='合格率')),
                ('assembly_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produce_form_ass_name', to='InfoManage.AssemblyLine', verbose_name='生产线')),
                ('hpro_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produce_form_hp_name', to='InfoManage.HalfProduct', verbose_name='半成品')),
            ],
            options={
                'verbose_name': '生产目标',
                'verbose_name_plural': '生产目标',
                'db_table': 'ProduceForm',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=8, verbose_name='产品名')),
                ('price', models.FloatField(verbose_name='价格')),
            ],
            options={
                'verbose_name': '产品',
                'verbose_name_plural': '产品',
                'db_table': 'Product',
            },
        ),
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rm_name', models.CharField(max_length=24, verbose_name='名称')),
                ('price', models.FloatField(verbose_name='价格')),
                ('classification', models.CharField(max_length=8, verbose_name='分类')),
                ('minimum_inventory', models.IntegerField(verbose_name='最小库存')),
                ('created', models.DateTimeField(verbose_name='创建时间')),
                ('updated', models.DateTimeField(verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '原材料',
                'verbose_name_plural': '原材料',
                'db_table': 'RawMaterial',
            },
        ),
        migrations.CreateModel(
            name='SaleForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sf_name', models.CharField(max_length=32, verbose_name='表名')),
                ('price', models.FloatField(verbose_name='价格')),
                ('created', models.DateTimeField(verbose_name='创建时间')),
                ('deliver_date', models.DateTimeField(verbose_name='交货时间')),
                ('state', models.BooleanField(default=0, verbose_name='是否发货')),
                ('check', models.BooleanField(default=0, verbose_name='是否确认')),
                ('out_stor_date', models.DateTimeField(verbose_name='出库时间')),
                ('c_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_form_c_name', to='InfoManage.Customer', verbose_name='客户')),
            ],
            options={
                'verbose_name': '销售订单',
                'verbose_name_plural': '销售订单',
                'db_table': 'SaleForm',
            },
        ),
        migrations.CreateModel(
            name='SaleFormProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='数量')),
                ('price', models.IntegerField(verbose_name='价格')),
                ('pro_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_form_product_pro_name', to='InfoManage.Product', verbose_name='产品')),
                ('sf_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_form_product_sf_name', to='InfoManage.SaleForm', verbose_name='销售订单')),
            ],
            options={
                'verbose_name': '订单产品',
                'verbose_name_plural': '订单产品',
                'db_table': 'SaleFormProduct',
            },
        ),
        migrations.CreateModel(
            name='Stor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=12, verbose_name='仓库名')),
                ('valid', models.BooleanField(default=1, verbose_name='可用')),
            ],
            options={
                'verbose_name': '仓库',
                'verbose_name_plural': '仓库',
                'db_table': 'Stor',
            },
        ),
        migrations.CreateModel(
            name='StorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_name', models.CharField(max_length=12, verbose_name='货物名称')),
                ('num', models.IntegerField(verbose_name='数量')),
                ('s_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stor_detail_s_name', to='InfoManage.Stor', verbose_name='仓库')),
            ],
            options={
                'verbose_name': '仓库详情',
                'verbose_name_plural': '仓库详情',
                'db_table': 'StorDetail',
            },
        ),
        migrations.CreateModel(
            name='SwapForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sf_name', models.CharField(max_length=48, verbose_name='表名')),
                ('created', models.DateTimeField(verbose_name='创建时间')),
                ('finished', models.DateTimeField(verbose_name='完成时间')),
                ('check', models.BooleanField(default=0, verbose_name='是否确认')),
                ('after_s_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swap_form_s_name', to='InfoManage.Stor', verbose_name='目标仓库')),
                ('before_s_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swap_form_old_s_name', to='InfoManage.Stor', verbose_name='原仓库')),
                ('staff_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swap_form_username', to=settings.AUTH_USER_MODEL, verbose_name='执行人')),
            ],
            options={
                'verbose_name': '货物调转表',
                'verbose_name_plural': '货物调转表',
                'db_table': 'SwapForm',
            },
        ),
        migrations.CreateModel(
            name='SwapFormDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='数量')),
                ('good_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swap_form_detail_good_name', to='InfoManage.StorDetail', verbose_name='货物名')),
                ('sf_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swap_form_detail_sf_name', to='InfoManage.SwapForm', verbose_name='调转表')),
            ],
            options={
                'verbose_name': '调转货物',
                'verbose_name_plural': '调转货物',
                'db_table': 'SwapFormDetail',
            },
        ),
        migrations.CreateModel(
            name='Vender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ven_name', models.CharField(max_length=24, verbose_name='名称')),
                ('addr', models.CharField(max_length=24, verbose_name='地址')),
                ('tel', models.CharField(max_length=12, verbose_name='电话')),
                ('created', models.DateTimeField(verbose_name='创建时间')),
                ('updated', models.DateTimeField(verbose_name='更新时间')),
                ('rm_name', models.ManyToManyField(to='InfoManage.RawMaterial', verbose_name='原材料')),
            ],
            options={
                'verbose_name': '供货商',
                'verbose_name_plural': '供货商',
                'db_table': 'Vender',
            },
        ),
        migrations.CreateModel(
            name='WasteForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='数量')),
                ('pf_name', models.IntegerField(verbose_name='生产目标表')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waste_form_good_name', to='InfoManage.StorDetail', verbose_name='材料')),
            ],
            options={
                'verbose_name': '废料表',
                'verbose_name_plural': '废料表',
                'db_table': 'WasteForm',
            },
        ),
        migrations.AddField(
            model_name='saleform',
            name='s_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_form_s_name', to='InfoManage.Stor', verbose_name='仓库'),
        ),
        migrations.AddField(
            model_name='saleform',
            name='staff_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_form_username', to=settings.AUTH_USER_MODEL, verbose_name='执行人'),
        ),
        migrations.AddField(
            model_name='produceform',
            name='pro_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produce_form_pro_name', to='InfoManage.Product', verbose_name='成品'),
        ),
        migrations.AddField(
            model_name='produceform',
            name='s_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produce_form_s_name', to='InfoManage.Stor', verbose_name='仓库'),
        ),
        migrations.AddField(
            model_name='outstorform',
            name='after_s_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='out_store_form_s_name', to='InfoManage.Stor', verbose_name='原仓库'),
        ),
        migrations.AddField(
            model_name='outstorform',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='out_store_form_username', to=settings.AUTH_USER_MODEL, verbose_name='执行人'),
        ),
        migrations.AddField(
            model_name='outstordetail',
            name='good_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='out_store_detail_good_name', to='InfoManage.StorDetail', verbose_name='货物名'),
        ),
        migrations.AddField(
            model_name='outstordetail',
            name='osf_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='out_store_detail_osf_name', to='InfoManage.OutStorForm', verbose_name='出库表'),
        ),
        migrations.AddField(
            model_name='orderformgoods',
            name='rm_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_form_goods_rm_name', to='InfoManage.RawMaterial', verbose_name='材料'),
        ),
        migrations.AddField(
            model_name='orderform',
            name='s_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_form_s_name', to='InfoManage.Stor', verbose_name='仓库'),
        ),
        migrations.AddField(
            model_name='orderform',
            name='ven_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_form_ven_name', to='InfoManage.Vender', verbose_name='供货商'),
        ),
        migrations.AddField(
            model_name='meterial',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meterial_good_name', to='InfoManage.StorDetail', verbose_name='材料'),
        ),
        migrations.AddField(
            model_name='meterial',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meterial_pro_name', to='InfoManage.Product', verbose_name='成品'),
        ),
    ]