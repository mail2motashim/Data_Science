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
df.insert(10,'Age_months',0)
def converter(val):
    value=val/12
    return value
df['Age_months']=converter(df['Age'])
df['Age_months']=round(df['Age_months'],1)
print(df['Age_months'])


#EDA


df1=df.copy()

#frequency Table

pd.crosstab(index=df1['FuelType'],columns='count',dropna=True)
pd.crosstab(index=df1['MetColor'],columns='count',dropna=True)

#two way tables
pd.crosstab(index=df1['Automatic'],columns=df1['FuelType'],dropna=True)

#two way table-joint probability
#two independent events happened at same time
pd.crosstab(index=df1['Automatic'],columns=df1['FuelType'],normalize=True,dropna=True)

#two way table-marginal probability
#single independent event
pd.crosstab(index=df1['Automatic'],columns=df1['FuelType'],margins=True,normalize=True,dropna=True)

#two way table-conditional probability
pd.crosstab(index=df1['Automatic'],columns=df1['FuelType'],margins=True,normalize='index',dropna=True)
#row sum in case of conditional probability is 1

pd.crosstab(index=df1['Automatic'],columns=df1['FuelType'],margins=True,normalize='columns',dropna=True)

#correlation
#visual correlation-scatter plot
#pearson Correlation
numeric_data=df1.select_dtypes(exclude=[object])
print(numeric_data.shape)
corr_matrix=numeric_data.corr()


#Data Visualization


#removing missing values fromthe database

df1.dropna(axis=0,inplace=True)
import numpy as np
import matplotlib.pyplot as plt

#scatter plot Age vs Price

plt.scatter(df1['Age'],df1['Price'],c='Red')
plt.title('Scatter plot Age vs Price')
plt.xlabel('Age(in months)')
plt.ylabel('Price(in Euros)')
plt.show()
 
#Histogram -represent frequency distribution of numerical values

plt.hist(df1['KM'],color='green',edgecolor='black',bins=5)
plt.title('Histogram of KM')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

#BarPlot

#represent frequency distribution of categorical values
#compare sets of data in different groups

counts=[979.120,12]
FuelType=['Petrol','Diesel','CNG']
index=np.arange(len(FuelType))
plt.bar(df1['Age'],df1['Price'],color=['blue','green'])
plt.title('Bar Chart')
plt.xlabel('Fuel Types')
plt.ylabel('Frequency')
plt.show()

#Seaborn library
import seaborn as s
#scatter plot (regresion) Age vs Price

s.set(style='darkgrid')
s.regplot(x=df1['Age'],y=df1['Price']) #by dfault fit reg is true
s.regplot(x=df1['Age'],y=df1['Price'],fit_reg=False)
s.lmplot(x='Age',y='Price',data=df1,fit_reg=False,hue='FuelType',legend=True,palette='Set1')


#Histogram (distributed plot)

s.distplot(df1['Age'])
s.distplot(df1['Age'],kde=False)
#control no of bins(range or interval)
s.distplot(df1['Age'],kde=False,bins=5)

#bar plot(count plot)

s.countplot(x='FuelType',data=df1)

# grouped bar plot fueltype vs Automatic

s.countplot(x='FuelType',data=df1,hue='Automatic')

#box plot and whiskers plot 5 number summary
s.boxplot(y=df1['Price'])
s.boxplot(x=df1['FuelType'],y=df1['Price'])

#grouped box plot and whiskers plot 

s.boxplot(x='FuelType',y=df1['Price'],hue='Automatic',data=df1)

#two plots in same window
f,(ax_box,ax_hist)=plt.subplots(2,gridspec_kw={'height_ratios':(.15,.85)})
s.boxplot(y=df1['Price'],ax=ax_box)
s.distplot(df1['Price'],ax=ax_hist,kde=False)

#pairwise plot

s.pairplot(df1,kind='scatter',hue='FuelType')
plt.show()
