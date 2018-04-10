# coding: utf-8

import requests
import pymysql


HOSTNAME = '127.0.0.1'
USERNAME = 'root'
PASSWORD = ''
DATABASE = 'pydata'


brand = 'http://www.autohome.com.cn/ashx/AjaxIndexCarFind.ashx?type=1'
series = 'http://www.autohome.com.cn/ashx/AjaxIndexCarFind.ashx?type=3&value={}'
model = 'http://www.autohome.com.cn/ashx/AjaxIndexCarFind.ashx?type=5&value={}'


def obtain_brand_info():
    request_brand = requests.get(brand)
    if request_brand.status_code == 200:
        request_brand.close()
        brand_json = request_brand.json()
        if brand_json['returncode'] == 0:  # 成功
            brand_list = brand_json['result']['branditems']
            conn = pymysql.connect(HOSTNAME, USERNAME, PASSWORD, DATABASE, charset="utf8")
            cur = conn.cursor()
            args = []
            for item in brand_list:  # 存入数据库 将 dict 转为 list
                sub_arg = (item['id'], item['name'], item['bfirstletter'])
                args.append(sub_arg)
            # print(args)
            # rowcount = cur.executemany('INSERT INTO auto_home_car_brand(brandid,name,bfirstletter) values(%s,%s,%s)', args)
            # conn.commit()
            # print(u"插入品牌:\n共{len(brand_dict)}\n成功插入{rowcount}条记录\n插入失败{len(brand_dict) - rowcount}条")
            # cur.close()
            # conn.close()
            # print brand_list
            return brand_list
    else:
        raise Exception("请求失败")


def obtain_series(brand_list):
    for brand_info in brand_list:
        request_series = requests.get(series.format(brand_info['id']))
        if request_series.status_code == 200:
            request_series.close()
            series_json = request_series.json()
            if series_json['returncode'] == 0:  # 成功
                factory_list = series_json['result']['factoryitems']
                conn = pymysql.connect(HOSTNAME, USERNAME, PASSWORD, DATABASE, charset="utf8")
                cur = conn.cursor()
                args = []
                series_count = 0
                for factory_item in factory_list:
                    factory_id = factory_item['id']
                    factory_name = factory_item['name']
                    series_items = factory_item['seriesitems']
                    for series_item in series_items:
                        series_count = series_count + 1
                        sub_arg = (brand_info['id'], factory_id, factory_name, series_item['id'], series_item['name'],
                                   series_item['seriesstate'], series_item['seriesorder'])
                        args.append(sub_arg)

                print args

                rowcount = cur.executemany('''INSERT INTO auto_home_car_series(brand_id, factory_id, `factory_name`, 
                                        `series_id`, `series_name`, `series_state`,`series_order`)
                                          values(%s, %s, %s, %s, %s, %s, %s)''',args)
                conn.commit()
                print(u"插入车系:\n共{series_count}\n成功插入{rowcount}条记录\n插入失败{series_count - rowcount}条")
                cur.close()
                conn.close()


def obtain_model():
    conn = pymysql.connect(HOSTNAME, USERNAME, PASSWORD, DATABASE, charset="utf8")
    cur = conn.cursor()
    cur.execute("select series_id from auto_home_car_series")
    series_list = cur.fetchall()

    for series in series_list:
        request_model = requests.get(model.format(series[0]))
        if request_model.status_code == 200:
            model_json = request_model.json()
            request_model.close()
            if model_json['returncode'] == 0:  # 成功
                year_items = model_json['result']['yearitems']
                conn = pymysql.connect(HOSTNAME, USERNAME, PASSWORD, DATABASE, charset="utf8")
                cur = conn.cursor()
                args = []
                model_count = 0
                for year_item in year_items:
                    for spec_item in year_item['specitems']:
                        model_count = model_count + 1
                        sub_args = (series[0], year_item['id'], year_item['name'], spec_item['id'], spec_item['name'],
                                    spec_item['state'], spec_item['minprice'], spec_item['maxprice'])
                        args.append(sub_args)

                rowcount = cur.executemany('''INSERT INTO auto_home_car_model(
                        `series_id`, `year_id`, `year_name`, `model_id`,
                        `model_name`, `model_state`, `min_price`, `max_price`)
                    values(%s, %s, %s, %s, %s, %s, %s, %s)''', args)
                conn.commit()
                print(u"插入车型:\n共{model_count}\n成功插入{rowcount}条记录\n插入失败{model_count - rowcount}条")
                cur.close()
                conn.close()



def main():
    # brand_list = obtain_brand_info()
    # obtain_series(brand_list)
    obtain_model()


if '__main__' == __name__:
    main()