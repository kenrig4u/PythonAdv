# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 17:24:04 2018

@author: SilverDoe
"""

'''
>>Pandas is an open-source Python Library used for high-performance data manipulation
 and data analysis using its powerful data structures.
 
>> It can load, organize, manipulate, model, and analyse the data.

>> Python deals with the following data structures :
    
    1. Series - 1D labeled homogeneous array, sizeimmutable, value mutable.
    2. DataFrame - General 2D labeled, value and size-mutable tabular structure with potentially heterogeneously typed columns.
    3. Panel - General 3D labeled, value and size-mutable array.
    
    higher dimensional data structure is a container of its lower dimensional data structure
    ========================================================================================
    >>DataFrame is a container of Series.
    >>Panel is a container of DataFrame.
    
    
    
============================== Series =========================================

pandas.Series( data, index, dtype, copy)
pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)

parameters
==========
	
1. data : data takes various forms like ndarray, list, constants.

2. index : Index values must be unique and hashable, same length as data. Default
           np.arrange(n) if no index is passed.
     
3. 	dtype : dtype is for data type. If None, data type will be inferred.

4. copy : Copy data. Default False
'''
#=============== Empty Series =================================================

import pandas as pd
s = pd.Series()
print(s)


#============= Series from ndarray ============================================

# no index passed
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)

# index passed
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print(s)

#========== Series from Dictionary ============================================

#No index given. Dictionary keys are used to construct index
import pandas as pd
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print(s)

#Index given. Index order is persisted and the missing element is filled with NaN
import pandas as pd
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print(s)

#=========== Series from Scalar ===============================================

import pandas as pd
s = pd.Series(5, index=[0, 1, 2, 3])
print(s)

#=========== Accessing data from series with position or index ================
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve data
print(s[0]) # using position
print(s['b']) # using index
print(s[:3]) # retreiving the first 3 elements in the series
print(s[-3:]) # last three elements
print(s[['a','c','d']]) # retreiving multiple values

































