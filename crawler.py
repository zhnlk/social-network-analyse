# -*- coding: utf-8 -*-
"""
01-爬取机构持有数据
Created on Tue Feb 26 20:31:28 2019
@author: Lin
"""
import requests
import json
import pandas as pd
import numpy as np
## 设置参数
# 导入csv数据，获取A股所有股票代码
df=pd.read_csv('C://Users//Administrator//Desktop//PC//stocks.csv',error_bad_lines=False)  
codes=list(df['code']) 
# 定义总数据集
data = [] 
#机构流通股持有占比限制、机构持有流通市值
ratio = 0.01 
value = 1000000
# 所有报告期、机构类型
times = ['2018-12-31','2018-09-30','2018-06-30','2018-03-31',   
         '2017-12-31','2017-09-30','2017-06-30','2017-03-31',
         '2016-12-31','2016-09-30','2016-06-30','2016-03-31',
         '2015-12-31','2015-09-30','2015-06-30','2015-03-31'] 
hold_class = ['基金','QFII','社保','保险','券商','信托'] 
## 获取并储存数据
# 爬数据
def get_data(url):
    #url = 'http://datainterface3.eastmoney.com/EM_DataCenter_V3/api/ZLCCMX/GetZLCCMX?tkn=eastmoney&SHType=&SHCode=&SCode=000001.sz&ReportDate=2018-09-30&sortField=SHCode&sortDirec=1&pageNum=1&pageSize=1000&cfg=ZLCCMX'
    r = requests.get(url)
    jsonObj = json.loads(r.content.decode('utf-8'))
    data0 = jsonObj['Data'][0]['Data']
    data = []
    for i in data0:
        data.append(i.split('|'))
    return data  
for i in range(len(codes)):
    url = 'http://datainterface3.eastmoney.com/EM_DataCenter_V3/api/ZLCCMX/GetZLCCMX?tkn=eastmoney&SHType=&SHCode=&SCode=%s&ReportDate=2018-09-30&sortField=SHCode&sortDirec=1&pageNum=1&pageSize=1000&cfg=ZLCCMX'% (str(codes[i]))
    data_1 = get_data(url)
    data.append(data_1)   
# 写入json文件
path = 'C://Users//Administrator//Desktop//PC//data_18_9_30.json'
s = json.dumps(data,indent=4,ensure_ascii=False)
with open(path, 'w', encoding = 'utf-8') as f:
    f.write(s)   
# 读取json数据
data = []  
path = 'C://Users//Administrator//Desktop//PC//data_18_9_30.json'
with open(path,encoding='utf-8') as f:
    s=f.read()
data=json.loads(s)
