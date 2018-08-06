# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 00:05:21 2018

@author: SilverDoe
"""

# Read Excel
import pandas as pd
 
df = pd.read_excel('E:\\Documents\\PythonProjects\\1_Basics\DataForFiles\\grades.xlsx', sheet_name='Sheet1')
print(df.columns)
print(df['Mark1'])

# Iterate over rows
for i in df.index:
    print(df['Mark1'][i])
    
    
# Write Excel
df.to_excel('E:\\Documents\\PythonProjects\\1_Basics\DataForFiles\\wexe.xlsx', sheet_name='Sheet1')