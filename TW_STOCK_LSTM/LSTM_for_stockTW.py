#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[76]:


close = pd.read_csv('close.csv')
close = close.transpose()
close = close.reindex(columns=close.columns[::-1])
close = close.drop(index = 'Unnamed: 0')


# In[96]:





# In[139]:


#做x資料 大X是array
xclose = []
xclose_train = []
xclose_test = []

n=3649
for times in range(3649):
    x_min =[]
    for i in close.loc[:,n]:
        try:
            data = float(i)
        except:
            data = float('nan')
        x_min.append(data)
    xclose.append(x_min)
    n = n-1

xclose_train=xclose[0:3000]
xclose_test =xclose[3000:3600]

Xclose_train = np.array(xclose_train)
Xclose_test = np.array(xclose_test)


# In[140]:


#做y資料 大Y是array
yclose = xclose[7:3607]
yclose_train = yclose[0:3000]
yclose_test = yclose[3000:3600]

Yclose_train = np.array(yclose_train)
Yclose_test = np.array(yclose_test)


# In[143]:


print(len(xclose_test),len(yclose_test),len(xclose_train),len(yclose_train))


# In[238]:


Xclose_train = Xclose_train.reshape(3000,1156,1)
Xclose_test = Xclose_test.reshape(600,1156,1)


# In[ ]:





# ##開始做model

# In[239]:


import tensorflow
import keras
from keras.models import Sequential
from keras.layers import Dense, BatchNormalization, LSTM, TimeDistributed


# In[243]:


model = Sequential()
model.add(LSTM(100, input_shape=(1156, 1), return_sequences = True))
model.add(LSTM(100))
model.add(Dense(1156,activation='relu'))
model.summary()


# model.summary()

# In[244]:


model.compile(loss='mse',optimizer = 'Adagrad', metrics=['acc'])


# In[245]:


model.fit(Xclose_train, Yclose_train, batch_size=7, epochs = 30)


# In[ ]:





# In[ ]:





# In[ ]:
