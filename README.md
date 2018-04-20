# 汽车之家 autohome
汽车之家车型库抓取，python抓取 车型


----------
项目演示：


----------
项目过程：




----------
服务依赖包：
>requests

>pymysql

>BeautifulSoup

>lxml

>htmllib

>re

>json

>sys


----------
项目运行：

python 版本： python-2.7.6









----------
项目说明：
>抓取汽车之家的品牌、车型、车款信息

>品牌 brand

>车系 series

>车型：model_type 发动机 年款 价格 颜色 外观


----------

车型配置文件：

>default_config.py

configs = dict()
configs = {
    'full_type_name':{'name': u'车型名称', 'field': 'full_type_name'},
    'firm_price':{'name': u'厂商指导价(元)', 'field': 'firm_price'},
    'firm':{'name': u'厂商', 'field': 'firm'},
    'grade':{'name': u'级别', 'field': 'grade'},
    'engine':{'name': u'发动机', 'field': 'engine'},
    'gear_box':{'name': u'变速箱', 'field': 'gear_box'},
    'cubage':{'name': u'长*宽*高(mm)', 'field': 'cubage'},
    'detail_body_structure':{'name': u'车身结构', 'field': 'detail_body_structure'},
    'max_speed':{'name': u'最高车速(km/h)', 'field': 'max_speed'},
    'official_acceleration':{'name': u'官方0-100km/h加速(s)', 'field': 'official_acceleration'},
    'measure_acceleration':{'name': u'实测0-100km/h加速(s)', 'field': 'measure_acceleration'},
    'measure_brake':{'name': u'实测100-0km/h制动(m)', 'field': 'measure_brake'},
    'measure_fuel_consumption':{'name': u'实测油耗(L/100km)', 'field': 'measure_fuel_consumption'},
    'combine_fuel_consumption':{'name': u'工信部综合油耗(L/100km)', 'field': 'combine_fuel_consumption'},
    'vehicle_warranty':{'name': u'整车质保', 'field': 'vehicle_warranty'},
    'car_length':{'name': u'长度(mm)', 'field': 'car_length'},
    'car_width':{'name': u'宽度(mm)', 'field': 'car_width'},
    'car_height':{'name': u'高度(mm)', 'field': 'car_height'},
    'wheelbase':{'name': u'轴距(mm)', 'field': 'wheelbase'},
    'front_track':{'name': u'前轮距(mm)', 'field': 'front_track'},
    'rear_track':{'name': u'后轮距(mm)', 'field': 'rear_track'},
    'min_ground_clearance':{'name': u'最小离地间隙(mm)', 'field': 'min_ground_clearance'},
    'curb_weight':{'name': u'整备质量(kg)', 'field': 'curb_weight'},
    'body_structure':{'name': u'车身结构', 'field': 'body_structure'},
    'door_number':{'name': u'车门数(个)', 'field': 'door_number'},
    'seat_number':{'name': u'座位数(个)', 'field': 'seat_number'},
    'tank_capacity':{'name': u'油箱容积(L)', 'field': 'tank_capacity'},
    'luggage_volume':{'name': u'行李厢容积(L)', 'field': 'luggage_volume'},
    'engine_model':{'name': u'发动机型号', 'field': 'engine_model'}
	.....