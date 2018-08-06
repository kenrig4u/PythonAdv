# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:30:07 2018

@author: SilverDoe
"""

'''

There are two kinds of sorting available in Pandas : 
    
    1. By Label
    2. By Actual Value

'''


'''================== Sorting By Label ========================================'''

import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns = ['col2','col1'])

# based on row index
sorted_df=unsorted_df.sort_index(axis=0,ascending=True)# ascending order. # ascending is true by default,axis = 0 by default
print(sorted_df) 
sorted_df = unsorted_df.sort_index(axis=0,ascending=False) # descending order
print(sorted_df)

#based on columns
sorted_df=unsorted_df.sort_index(axis=1,ascending=True)# ascending order
print(sorted_df) 
sorted_df = unsorted_df.sort_index(axis=1,ascending=False) # descending order
print(sorted_df)



'''=================== Sorting By Value ======================================='''

'''

Like index sorting, sort_values() is the method for sorting by values. It accepts
 a 'by' argument which will use the column name of the DataFrame with which the 
 values are to be sorted

'''

import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
   
# based on a specific column
sorted_df = unsorted_df.sort_values(by='col1')
print(sorted_df)

# based on multiple columns
sorted_df = unsorted_df.sort_values(by=['col1','col2'])
print(sorted_df)

# specifying sorting alorithm
sorted_df = unsorted_df.sort_values(by='col1' ,kind='mergesort') # mergesort, heapsort and quicksort
print(sorted_df)













