# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 09:34:37 2018

@author: SilverDoe
"""

'''
========================== DataFrame ==========================================

pandas.DataFrame( data, index, columns, dtype, copy)

Parameters : 
============
1. data : data takes various forms like ndarray, series, map, lists, dict, constants
   and also another DataFrame.
   
2. index : For the row labels, the Index to be used for the resulting frame is 
   Optional Default np.arrange(n) if no index is passed.
   
3. columns : For column labels, the optional default syntax is - np.arrange(n). 
   This is only true if no index is passed.
   
4. dtype : Data type of each column.

5. copy : This command (or whatever it is) is used for copying of data, if the 
   default is False.
   

'''

#=============== Empty DataFrame =================================================

import pandas as pd
df = pd.DataFrame()
print(df)

#============= DataFrame from Lists ============================================

# no index passed, no column names given
import pandas as pd
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

# no index passed, column names given
import pandas as pd
data = [['Natsu',13],['Lisanna',9],['Happy',1]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)

# no index passed, column names given, datatype passed
import pandas as pd
data = [['Natsu',13],['Lisanna',8],['Happy',1]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print(df)


#========== Dataframe from Dictionary of ndarrays/lists ============================================

''' 
>>All the ndarrays must be of same length. If index is passed, then the length
 of the index should equal to the length of the arrays.
 
>> To preserve the order of the columns:
    1. use ordered doctionary, since dictionaries will not preserve the order when created. 
    2. use columns index while creating the dataframe.
    3. use  reorder the columns the way you want by using df = df[list of column names in the order you want]
 
'''
 
# using arrays, No index given.
import pandas as pd
data = {'Name':['Lisanna', 'Natsu', 'Erza', 'Gray'],'Age':[15,20,23,20]}
df = pd.DataFrame(data)
print(df)

# using arrays, Index given. 
import pandas as pd
data = {'Name':['Lisanna', 'Natsu', 'Erza', 'Gray'],'Age':[15,20,23,20]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)

'''
>>List of Dictionaries can be passed as input data to create a DataFrame. The 
dictionary keys are by default taken as column names.

>>NaN (Not a Number) is appended in missing areas when using lists instead of arrays.

'''

# using lists, no index given
import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)

# using lists,index given
import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
print(df)

# using lists,index given, columns given
import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
print(df1)

#With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print(df2)


#using dictionary of Series
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)


# using ordered dictionary to preserve the order of the columns
import numpy as np
import pandas as pd
from collections import OrderedDict

a = np.array( [ 1, 2, 3 ] )
b = np.array( [ 4, 5, 6 ] )
c = np.array( [ 7, 8, 9 ] )

nd = { 'p': pd.Series(a), 'z': pd.Series(b), 'n': pd.Series(c) } # normal dictionary
od = OrderedDict( { 'p': pd.Series(a), 'z': pd.Series(b), 'n': pd.Series(c) } ) # ordered doctionary

df = pd.DataFrame(od)
print(df)












