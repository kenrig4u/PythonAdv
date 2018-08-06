# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 19:28:13 2018

@author: SilverDoe
"""

import pandas as pd

df= pd.read_excel('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\grades.xlsx') #Reading the dataset in a dataframe using Pandas
df2 = df.set_index("Student Name", drop = True)
df2.head(4)
#df.drop(df.columns[[0]], axis=1, inplace=True)

df.describe()
df['Mark1'].value_counts()

per = []

for i in range(2,len(df)+2):
    per.append('=SUM(A'+str(i)+':F'+str(i)+')/'+str(len(df)))

df['Percentage'] = per

df.to_excel('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\grades.xlsx',index = False)

