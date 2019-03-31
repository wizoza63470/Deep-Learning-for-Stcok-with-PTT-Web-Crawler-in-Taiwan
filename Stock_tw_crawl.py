#!/usr/bin/env python
# coding: utf-8

# In[25]:


import requests
from io import StringIO
import pandas as pd
import numpy as np


# In[26]:


def crawl_price(date):
    r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + str(date).split(' ')[0].replace('-','') + '&type=ALL')
    ret = pd.read_csv(StringIO("\n".join([i.translate({ord(c): None for c in ' '})
                                        for i in r.text.split('\n')
                                        if len(i.split('",')) == 17 and i[0] != '='])), header=0)
    ret = ret.set_index('證券代號')
    ret['成交金額'] = ret['成交金額'].str.replace(',','')
    ret['成交股數'] = ret['成交股數'].str.replace(',','')
    return ret


# In[27]:


import datetime
import time

data = {}
n_days = 3650
date = datetime.datetime.today()
fail_count = 0
allow_continuous_fail_count = 5
while len(data) < n_days:

    print('parsing', date)
    # 使用 crawPrice 爬資料
    try:
        # 抓資料
        data[date] = crawl_price(date)
        print('success!')
        fail_count = 0
    except:
        # 假日爬不到
        print('fail! check the date is holiday')


    # 減一天
    date -= datetime.timedelta(days=1)
    time.sleep(10)


# In[ ]:





# In[15]:


close = pd.DataFrame({k:d['收盤價'] for k,d in data.items()}).transpose()
close.index = pd.to_datetime(close.index)
close.to_csv('close.csv')


# In[17]:


stockname = pd.DataFrame({k:d['證券名稱'] for k,d in data.items()}).transpose()
stockname.index = pd.to_datetime(stockname.index)
stockname.to_csv('stockname.csv')


# In[19]:


transaction = pd.DataFrame({k:d['成交筆數'] for k,d in data.items()}).transpose()
transaction.index = pd.to_datetime(transaction.index)
transaction.to_csv('transaction.csv')


# In[20]:


volume = pd.DataFrame({k:d['成交股數'] for k,d in data.items()}).transpose()
volume.index = pd.to_datetime(volume.index)
volume.to_csv('volume.csv')


# In[21]:


trans_money = pd.DataFrame({k:d['成交金額'] for k,d in data.items()}).transpose()
trans_money.index = pd.to_datetime(trans_money.index)
trans_money.to_csv('trans_money.csv')


# In[22]:


openprice = pd.DataFrame({k:d['開盤價'] for k,d in data.items()}).transpose()
openprice.index = pd.to_datetime(openprice.index)
openprice.to_csv('openprice.csv')


# In[23]:


high = pd.DataFrame({k:d['最高價'] for k,d in data.items()}).transpose()
high.index = pd.to_datetime(high.index)
high.to_csv('high.csv')


# In[24]:


low = pd.DataFrame({k:d['最低價'] for k,d in data.items()}).transpose()
low.index = pd.to_datetime(low.index)
low.to_csv('low.csv')


# In[ ]:





# In[ ]:





# # 做deep learning的data

# In[1]:





# In[ ]:
