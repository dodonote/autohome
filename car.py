# encoding:utf-8
# ------------------------------------------------
#    作用：抓取汽车之家车型库
#    日期：2018-03-25
#    作者：呆呆
# ------------------------------------------------


import requests
import pymysql
from bs4 import BeautifulSoup
import lxml
import htmllib
import re
import json
import sys

import config_default

configs = config_default.configs

# print configs['full_type_name']['name']

# print configs

# exit()

# print configs.items()

# for key,values in configs.items():
#     print values['name']
# exit
# print 123
# exit()

reload(sys)

sys.setdefaultencoding('utf-8')

HOSTNAME = '127.0.0.1'
USERNAME = 'root'
PASSWORD = ''
DATABASE = 'pydata'

conn = pymysql.connect(HOSTNAME, USERNAME, PASSWORD, DATABASE, charset="utf8")
cur = conn.cursor()


# print cur

brandUrl = 'https://car.autohome.com.cn'
seriesUrl = 'https://car.autohome.com.cn/price/series-{}.html'
modelUrl = 'https://car.autohome.com.cn/config/spec/{}.html#pvareaid={}'

# BeautifulSoup用法
'''
soup = BeautifulSoup("<html>data</html>","lxml")
soup = BeautifulSoup('<b name="test" class="boldest">Extremely bold</b>','lxml')
tag = soup.b
# print tag
# print soup.prettify()
# print soup.body
# print type(soup.b)
print soup.name
print soup.b.attrs
print soup.b['class']
print soup.string

print soup.b
print soup.b.string
print type(soup.b.string)

print soup.find_all('b')
soup.find_all(["a", "b"])
soup.find_all("a", limit=2)
soup.find_all(id='link2')

soup.find_all(href=re.compile("elsie"))
soup.find_all("a", class_="sister")
soup.find_all(href=re.compile("elsie"), id='link1')

soup.html.find_all("title")
soup.find_all('b')

print soup.select('#link1')
print soup.select('title')
print soup.select('p #link1')
print soup.select("head > title")
print soup.select('a[class="sister"]')
print soup.select('.sister')

html = ''
soup = BeautifulSoup(html, 'lxml')
print type(soup.select('title'))
print soup.select('title')[0].get_text()

for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

for title in soup.select('title'):
    print title.get_text()
'''

def get_brand():
    res = requests.get('https://car.autohome.com.cn/AsLeftMenu/As_LeftListNew.ashx?typeId=1%20&brandId=0%20&fctId=0%20&seriesId=0')
    # print res
    if res.status_code == 200:
        res.close()
        soup = BeautifulSoup(res.text, 'lxml')

        # for letter in soup.find_all(class_="cartree-letter"):
        #     print letter.get_text()

        data = []
        for letter in soup.select(".cartree-letter"):
            # print args.get("href")
            # print letter.find_next()
            for li in letter.find_next():
                args = li.find("a")
                sub_arg = (letter.get_text(),args['href'],re.findall(u".*\(", args.get_text())[0].replace("(",""),re.findall(u"\d+\.?\d*", args.find("em").get_text())[0])
                data.append(sub_arg)

                # print li


        # rowcount = cur.executemany('INSERT INTO car_brand (firstletter,linkurl,name,carnum) values(%s,%s,%s,%s)', data)
        # conn.commit()
        #
        # cur.close()
        # conn.close()

        # print data

        return data

def obtain_brand():
    res = requests.get(brandUrl)
    # print request_brand
    # print res.url
    # res.encoding = 'utf-8';
    # print res.encoding
    # print res.raw
    # print res.json()
    if res.status_code == 200:
        res.close()
        res.encoding = 'gb2312'
        resHtml = res.text

        # print resHtml
        soup = BeautifulSoup(resHtml,'lxml')
        # print soup
        # print soup.title
        # print soup.title
        # print soup.find_all(id='cartree')
        # print soup.select("#cartree .cartree-letter")
        # print soup.select(".cartree-letter")

        # print soup.find_all("div")

        print soup.find_all(name='div', attrs={"class":"cartree"})

        for div in soup.find_all(name='div', attrs={"class":"cartree-letter"}):
            print div.get_text()

        for letter in soup.select("#cartree .cartree-letter"):
            print letter()

def obtain_series(data):

    host = 'https://car.autohome.com.cn'
    # print data

    for info in data:

        # print host + info[1]
        res = requests.get(host+info[1]);
        if res.status_code == 200:
            res.close()
        # res.encoding = 'gb2312'
        soup = BeautifulSoup(res.text, "lxml")

        # print soup.title

        level_name = ''
        for series in soup.select('div[class="carbradn-cont fn-clear"] dl'):

            firm = series.find('dt').get_text()
            firm_url = series.find('dt').find('a').get('href')

            # print firm

            for level in series.select("dd div"):

                # print level.attrs['class']
                if level.attrs['class'][0] == 'list-dl-text':
                    level_name = level.find_previous().get_text()
                    # print level_name
                    for model in level.select("a"):

                        model_name = model.get_text()
                        model_url = model.get("href")

                        # print firm,firm_url,level_name,model_name,model_url

                        # rowcount = cur.execute('INSERT INTO car_series (firm,firmurl,levelname,model,modelurl,brandurl) values(%s,%s,%s,%s,%s,%s)', (firm, firm_url, level_name, model_name, model_url, res.url))
                        # conn.commit()

                        result = obtain_model(re.findall("series-(\d+)[\.|-]",model_url)[0])
                        model_type_save(result)

    # cur.close()
    # conn.close()

def obtain_model(series_id):

    url = 'https://car.m.autohome.com.cn/ashx/car/GetModelConfigNew.ashx?seriesId={}'
    request_model = requests.get(url.format(series_id))
    #
    print request_model.url
    # print request_model.text
    # print request_model.json()
    # # print request_model.status_code
    # result = request_model.json()
    # print result
    # print result['param']

    if request_model.status_code == 200:
        model_json = request_model.json()
        request_model.close()
        # print  model_json['param']
        # print model_json
        year_items = model_json
        # print year_items

        dict_model = dict()
        args = []
        model_count = 0

        # print year_items
        for param in ['config','param']:

            # print param
            for year_item in year_items[param]:

                # print param
                for chile_item in year_item[param+'items']:

                    # print chile_item
                    valueName = chile_item['name']
                    valueItems = chile_item['valueitems']

                    # print chile_item
                    # print valueName
                    for key,values in configs.items():

                        # print key,values
                        if valueName == values['name']:
                            enName = key
                            break
                    #
                    # print enName

                    for spec_item in valueItems:

                        # print spec_item
                        model_count = model_count + 1

                        spec_id = spec_item['specid']
                        spec_name = spec_item['value']
                        # print spec_name

                        # sub_args = (spec_item[0], year_item['id'], year_item['name'], spec_item['id'], spec_item['name'],
                        #             spec_item['state'], spec_item['minprice'], spec_item['maxprice'])
                        # args.append(sub_args)

                        # print spec_name

                        # spec_name = spec_name
                        addtwodimdict(dict_model,spec_id,enName,spec_name)
                        # print "共{}条，名称{}，值{}".format(model_count,spec_id,spec_name)

                    # print valueItems
        # print dict_model
        return dict_model

#具体车款存储
def model_type_save(data):

    # print data

    values = []
    item_key = []
    pleis = []
    car_name = ''
    car_values = ''
    for key,item in data.items():
        # print key,values
        # print item.keys()
        # print item.values()

        # print len(item_key)
        if len(item_key) == 0:
            item_key = item.keys()
            # print item_key
            for i in item_key:
                pleis.append('%s')

            car_name = ",".join(item_key)

        values.append(tuple(item.values()))

    car_values = ",".join(pleis)

    # print car_name
    # print values
    # print car_values

    # str = 'INSERT INTO car_model_type('+car_name+') values('+car_values+')'
    # print str
    rowcount = cur.executemany('INSERT INTO car_model_type('+car_name+') values('+car_values+')', values)
    conn.commit()

    # cur.close()
    # conn.close()

#add 2d dict
def addtwodimdict(thedict, key_a, key_b, val):
    if key_a in thedict:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a:{key_b: val}})

def main():
    # for i in range(10):
    #     print(i,end=(','))
    result = get_brand()
    # obtain_brand()
    # print result
    obtain_series(result)
    # result = obtain_model(66)
    # model_type_save(result)

if '__main__' == __name__:
    main()