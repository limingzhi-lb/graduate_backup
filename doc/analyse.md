# 角色

## 采购(purchase)

采购员 purchase_agent

采购部主管 purchase_leader

## 仓库（多个）store

仓库管理员 store_agent

仓库主管 store_leader

## 生产 production

生产主管 production_leader

流水线负责人 assemblyline_leader

## 销售 sale

销售员 sale_agent

销售主管 sale_leader

# 数据库表

##采购类

### 供货商 vender

| field            | type        | index | isnull |
| ---------------- | ----------- | ----- | ------ |
|                  |             |       |        |
| 名称 ven_name    | varchar(24) | yes   | no     |
| 地址 addr        | varchar(32) | no    | no     |
| 电话 tel         | varchar(12) | no    | no     |
| 创建时间 created | datetime    | yes   | no     |
| 更新时间 updated | datetime    | yes   | no     |
| good_ids         | json        | no    | yes    |

主键：ven_name

### 原材料 RawMaterial

| field                      | type        | index | isnull |
| -------------------------- | ----------- | ----- | ------ |
|                            | integer     | yes   | no     |
| 名称 rm_name               | varchar(12) | yes   | no     |
| 价格 price                 | float       | no    | no     |
| 分类 classification        | char(8)     | yes   | no     |
| 最小库存 minimum_inventory | int(6)      | no    | no     |
| 批次号 batch_number        |             |       |        |
| 创建时间  updated          | datetime    | no    | no     |
| 更新时间 created           | datetime    | no    | no     |

主键：rm_name

### 购货单 OrderForm

| field                                        | type     | index | isnull         |
| -------------------------------------------- | -------- | ----- | -------------- |
| of_id                                        | integer  | yes   | no             |
| 供应商id ven_id                              | integer  | yes   | no             |
| 创建日期 created                             | datetime | no    | no             |
| 调入仓库（若退货可为空）                     | integer  | yes   | no (default:0) |
| 交货日期 delivery                            | datetime | no    | no             |
| 类型（购货1/退货0）typ                       | boolean  | yes   | no             |
| 收货状态（只能由仓库人员操作）receipt_status | boolean  | yes   | no             |
| 付款状态 payment_status                      | boolean  | yes   | no             |
| 总价（是否可有？）total_price                | float    | no    | no             |
| 执行人 executor                              | integer  | yes   | no             |
| 入库日期 storage_time                        | datetime | no    | yes            |
| 是否完成 is_finish                           | boolean  | yes   | no (default:0) |

主键：ord_form_id

### 购货单具体商品 OrdFormGoods

| field            | type    | index | isnull |
| ---------------- | ------- | ----- | ------ |
| 商品名 rm_id     | integer | yes   | no     |
| 购货单 of_id     | integer | yes   | no     |
| 数量 num         | integer | no    | no     |
|                  |         |       |        |
| 批次号 batch_num | char(8) | no    | yes    |

主键：rm_id, ord_form_id

## 仓库类

### 仓库 Stor

| field          | type    | index | isnull     |
| -------------- | ------- | ----- | ---------- |
| stor_id        | integer | yes   | no         |
| 仓库名 name    |         |       |            |
| 是否可用 valid | boolean | no    | default(1) |
|                |         |       |            |
| 主键：stor_id  |         |       |            |

### 调货单（货物在仓库之间调动）SwapForm

| field                  | type     | index | isnull     |
| ---------------------- | -------- | ----- | ---------- |
| sf_id                  | integer  | yes   | no         |
| 经办人 staff_id        | integer  | yes   | no         |
| 原仓库 before_stor_id  | integer  | yes   | no         |
| 调入仓库 after_stor_id | integer  | yes   | no         |
| 创建日期 created       | datetime | no    | no         |
| 完成日期 finished      | datetime | no    | yes        |
| 审核 check             | boolean  | no    | default(0) |
| 明细 sf_detail_id      | integer  | yes   | no         |

主键：sf_id

### 调货明细 SwapFormDetail

| field                                | type    | index | isnull     |
| ------------------------------------ | ------- | ----- | ---------- |
| sf_detail_id                         | integer | yes   | no         |
| 产品名称 good_name                   | integer | yes   | no         |
| 数量 num                             | integer | no    | no         |
| 批号（批号和数量要对应）batch_number | char(8) | no    | default(0) |
| 所属调货单 sf_id                     | integer | yes   | No         |
|                                      |         |       |            |

主键：sf_detail_id

### 出库单 OutStorForm

| field                  | type        | index | isnull     |
| ---------------------- | ----------- | ----- | ---------- |
| osf_id                 | integer     | yes   | no         |
| 单据日期 created       | datetime    | no    | no         |
| 调出仓库 after_stor_id | integer     | yes   | no         |
| 经办人 staff_id        | integer     | yes   | no         |
| 审核（是否）check      | boolean     | no    | default(0) |
| 备注 note              | varchar(64) | no    | yes        |
| 完成日期 finished      | datetime    | no    | yes        |
| 出库物品 osd_id        | json        | no    | no         |

主键：osf_id

### 出库明细 OutStorDetail

| field             | type        | index | isnull |
| ----------------- | ----------- | ----- | ------ |
| osd_id            | integer     | yes   | no     |
| 产品名称 name     | varchar(12) | yes   | no     |
| 数量 num          | integer     | no    | no     |
| 批号 batch_num    | char(8)     | no    | No     |
| 所属出库单 osf_id | integer     | yes   | no     |

主键：osd_id

## 生产

### 成品 Product

| field               | type     | index | isnull |
| ------------------- | -------- | ----- | ------ |
|                     |          |       |        |
| 名称 pro_name       | char(8)  | yes   | no     |
| 所需原材料及个数 rm | json     | no    | yes    |
| 所需半成品及个数 hp | json     | no    | yes    |
| 单价 price          | float(8) | no    | no     |
|                     |          |       |        |

### 半成品 HalfProduct

| field               | type    | index | isnull |
| ------------------- | ------- | ----- | ------ |
|                     |         |       |        |
| 名称 hp_name        | char(8) | yes   | no     |
| 所需原材料及个数 rm | json    | no    | yes    |
| 所需半成品及个数 hp | json    | no    | yes    |
|                     |         |       |        |
|                     |         |       |        |

### 生产单 ProduceForm

| field                                 | type     | index | isnull     |
| ------------------------------------- | -------- | ----- | ---------- |
| pf_id                                 | integer  | yes   | no         |
| 产品名 name                           | char(8)  | yes`  | no         |
| 数量 num                              | integer  | no    | no         |
| 日期 created                          | datetime | yes   | no         |
| 流水线 assembly_line                  | integer  | yes   | no         |
| 实际数量（流水线管理员）actual_num    | integer  | no    | yes        |
| 是否入库（仓库管理员）is_instor       | boolean  | no    | default(0) |
| 备注 note                             | text     | no    | yes        |
| 是否完成（由生产部主管决定）is_finish | boolean  | no    | default(0) |
| 仓库 stor_id                          | integer  | no    | yes        |
|                                       |          |       |            |
| 合格率  qualified_rate                | float    | yes   | no         |

### 废料单 WasteForm

| field            | type    | index | isnull |
| ---------------- | ------- | ----- | ------ |
|                  |         |       |        |
| 名称 name        | char(8) | yes   | no     |
| 数量 num         | integer | no    | no     |
| 所属生产单 pf_id | integer | yes   | no     |
|                  |         |       |        |
|                  |         |       |        |

## 销售

### 客户 Customer

| field      | type        | index | isnull |
| ---------- | ----------- | ----- | ------ |
|            |             |       |        |
| 名称 name  | varchar(24) | yes   | no     |
| 手机号 tel | varchar(12) | no    | no     |
| 地址 addr  | varchar(32) | no    | no     |
|            |             |       |        |

### 销售订单 SaleForm

| field                         | type     | index | isnull     |
| ----------------------------- | -------- | ----- | ---------- |
| sf_id                         | integer  | yes   | no         |
| 经办人 staff_id               | integer  | yes   | no         |
| 客户 c_id                     | integr   | yes   | no         |
| 价格 price                    | float    | no    | no         |
| 创建日期 created              | datetime | yes   | no         |
| 交货日期 deliver_date         | datetime | yes   | no         |
| 调出仓库 stor_id              | intger   | no    | no         |
| 发货状态（仓库人员权限）state | boolean  | yes   | default(0) |
| 商品 pro_name                 | json     | no    | no         |
| 审核（默认未审核）check       | boolean  | yes   | default(0) |
| 出库日期（仓库）out_stor_date | datetime | no    | yes        |

###订单商品 SaleFormProduct

| field           | type        | index | isnull |
| --------------- | ----------- | ----- | ------ |
| sf_id           | integer     | yes   | no     |
| price           |             |       |        |
| 商品名 pro_name | varchar(12) | yes   | no     |
| 数量 num        | integer     | no    | no     |



## 仓库详细 StorDetail

| field         | type        | index | isnull |
| ------------- | ----------- | ----- | ------ |
|               |             |       |        |
| 货物名 name   | varchar(12) | yes   | no     |
| 数量 num      | integer     | no    | no     |
| 所属仓库 s_id | integer     | yes   | no     |
|               |             |       |        |

## 部门（个数固定）department

| field    | type        | index | isnull |
| -------- | ----------- | ----- | ------ |
| id       | integer     | yes   | no     |
| category | integer     | yes   | no     |
| name     | varchar(24) | no    | no     |
|          |             |       |        |

##人员 Staff

| field          | type    | index | isnull |
| -------------- | ------- | ----- | ------ |
| s_id           | integer | yes   | no     |
| 工号 staff_num | integer | yes   | no     |
| 密码 hash      |         |       |        |
| 状态           |         |       |        |
|                |         |       |        |
|                |         |       |        |
| is_leader      |         |       |        |
| dep_id         |         |       |        |

##role

| field              | type        | index | isnull |
| ------------------ | ----------- | ----- | ------ |
| role_id            | integer     | yes   | no     |
| name               | varchar(24) | no    | no     |
| 权限列表permission | json        | no    | no     |

##org_role

| field        | type    | index | isnull |
| ------------ | ------- | ----- | ------ |
| role_id      | integer | yes   | no     |
| dep_category | integer | yes   | no     |
|              |         |       |        |

主键： role_id， dep_category

## user_permission

| field    | type        | index | isnull |
| -------- | ----------- | ----- | ------ |
|          |             |       |        |
| staff_id | integer     | yes   | no     |
| action   | varchar(24) | yes   | no     |
| resource | varchar(24) | yes   | no     |

联合主键： org_id，staff_num，action，resource

## RolePermission

| field      | type    | index | isnull |
| ---------- | ------- | ----- | ------ |
| role_id    | integer | yes   | no     |
| permission | json    | no    | yes    |
|            |         |       |        |



## UserRole

| field    | type    | index | isnull |
| -------- | ------- | ----- | ------ |
| Staff_id | integer | yes   | no     |
| Org_id   | integer | yes   | no     |
| Role_id  | integer | yes   | no     |
|          |         |       |        |

### 权限

order list,create,edit
swap list,create,edit
out list,create,edit
produce list,create,edit
waste list,create,edit
sale list,create,edit



# 流程

## 采购流程

采购主管有权限建立采购单，增加供货商和原材料，购货单分为购货和退货，购货时主管建立购货单，交货日期为最晚日期，由仓库人员管理收货状态和入库日期，然后采购主管确认完成

## 仓库

调货由仓库主管建立，选择一个经办人来操作

## 生成流程

生成部主管建立生成单，分配给流水线，每天结束由流水线管理员填写实际数量，废料，合格率。然后仓库管理员选择是否入库，最后生产部主管选择是否完成

## 销售

销售主管建立销售单，选择经办人，仓库管理员填写发货和出库日期，最后销售主管审核。





Tips:

user属于部门，部门有leader和员工，权限不一样