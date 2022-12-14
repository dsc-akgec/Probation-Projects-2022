# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l7Jp7Nb5JB9vXu6K9OWvb2u4QwkPTVr-
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('data.csv')
df.head()

"""# New Section"""

df.info();

df.isnull().sum()



df=df[~df.permit.isnull()].copy()
df.isnull().sum()
df=df[~df.admin.isnull()].copy()
df.isnull().sum()

"""# New Section"""

df.head(20)

plt.figure(figsize=(20, 5))

 plt.bar(df.state,df.handgun)
 plt.xticks(rotation=90)

 plt.legend

"""This Shows Florida and Texas has the most amount of Handgun permit checks in the US however this is a try run

"""

corr=df.corr()
plt.figure(figsize=(20,15))
sns.heatmap(corr,annot=True)

df.month=pd.to_datetime(df.month)
plt.figure(figsize=(20,8))
dt=df.groupby(pd.Grouper(key='month',freq='1Y'))['permit'].sum()

dt.plot(kind='bar')

plt.figure(figsize=(20,8))
dtt=df.groupby('state')['totals'].sum();
dtt.plot(kind='bar')

plt.figure(figsize=(20,10))
dt1=df.groupby('state')['multiple'].sum()
dt1.plot(kind='bar')

plt.figure(figsize=(20,10))
dt1=df.groupby('state')['other'].sum()
dt1.plot(kind='bar')

plt.figure(figsize=(20,9))
dt2=df.groupby(pd.Grouper(key='month',freq='4Y'))['totals'].sum()
dt2.plot(kind='bar')

dt2.head(40)

dt2.head(
    
)

plt.figure(figsize=(20,5))
dt2=df.groupby(pd.Grouper(key='month',freq='1Y'))['permit_recheck'].sum()
dt2.plot(kind='bar')



plt.figure(figsize=(20,9))
dt2=df.groupby(pd.Grouper(key='month',freq='1Y'))['permit_recheck'].sum()
dt2.plot(kind='bar')

dts=df
dts.isnull().sum()

dts=dts[~dts.permit_recheck.isnull()].copy()
dts.isnull().sum()

plt.figure(figsize=(10,8))
dt3=df.groupby('state')['handgun'].sum()
dtd=df.groupby('state')['long_gun'].sum()
plt.scatter(dt3,dtd)
plt.show()

plt.figure(figsize=(10,8))

dt5=df.groupby(pd.Grouper(key='month',freq='1Y'))['returned_handgun'].sum()
dt5.plot(kind='bar')

plt.figure(figsize=(15,10))
dt6=df.groupby('state')['private_sale_handgun'].sum()
dt6.plot(kind="bar")

