#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd

data1 = pd.read_csv('reviews1.csv')
data2 = pd.read_csv('reviews2.csv')
data = pd.concat([data1, data2])
data.to_csv('reviews.csv')

