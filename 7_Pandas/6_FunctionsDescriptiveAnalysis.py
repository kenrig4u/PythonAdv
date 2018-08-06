# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:42:44 2018

@author: SilverDoe
"""

'''
============= Functions for Descriptive Analysis ==============================

1. count()    : Number of non-null observations

2. sum()      : Sum of values

3.	mean()	     : Mean of Values

4.	median()   : Median of Values

5.	mode()	     : Mode of values

6.	std()      : Standard Deviation of the Values

7.	min()      : Minimum Value

8.	max()      : Maximum Value

9.	abs()      : Absolute Value

10.	prod()	     : Product of Values

11.	cumsum()   : Cumulative Sum

12.	cumprod()  : Cumulative Product

'''

import pandas as pd
 
#Create a Dictionary of series
d = {'Name':pd.Series(['Natsu','Lisanna','Gray','Lucy','Erza','Elfman','Mirajane',
   'Wendy','Gaara','Hashirama','Madara','Nagato']),
   'Age':pd.Series([20,15,20,20,23,22,23,22,21,54,54,29]),
   'Rating':pd.Series([5,5,4.9,4.9,4.9,4.6,4.6,4.6,4.7,4.80,2.12,4.9])}


df = pd.DataFrame(d)
print(df.sum())
print(df.mean())
print(df.median())
print(df.mode())
print(df.std())
print(df.min())
print(df.max())
print(df.abs()) # TypeError Exception thrown... does not work when there are strings
print(df.prod())
print(df.cumsum())
print(df.cumprod()) # TypeError Exception thrown... does not work when there are strings
print(df.describe()) #  computes a summary of statistics
print(df.describe(include=['object'])) # Summarizes String columns
print(df.describe(include=['number'])) # Summarizes Numeric columns
print(df.describe(include='all'))












