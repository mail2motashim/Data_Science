# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 14:03:10 2023

@author: Admin
"""

import pandas as pd
df=pd.read_csv("C:\\Users\\Admin\\OneDrive\\Desktop\\desktop\\IMP\\NPTEL\\Python for DS\\practise\\Toyota.csv",index_col=0,na_values=["????","??"])
df.info()
import numpy as np
np.unique(df['Doors'])
df['Doors'].replace('three',3,inplace=True)
df['Doors'].replace('five',5,inplace=True)
df['Doors'].replace('four',4,inplace=True)
df['Doors']=df['Doors'].astype('int64')
np.unique(df['Doors'])
df.isnull().sum()
df.insert(10,'Price_Class','')
for i in range(0,len(df['Price']),1):
    if df['Price'][i]<8450:
        df['Price_Class'][i]='low'
    elif df['Price'][i]>11950:
        df['Price_Class'][i]='high'
    else:
        df['Price_Class'][i]='medium'
while i <len(df['Price']):
    if df['Price'][i]<8450:
        df['Price_class'][i]='LOW'
    elif df['Price'][i]>11950:
        df['Price_class'][i]='HIGH'
    else:
        df['Price_class'][i]='MEDIUM'