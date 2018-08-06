# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:15:43 2018

@author: SilverDoe
"""

'''

The behavior of basic iteration over Pandas objects depends on the type. When iterating 
over a Series, it is regarded as array-like, and basic iteration produces the values.
 Other data structures, like DataFrame and Panel, follow the dict-like convention
 of iterating over the keys of the objects.
 
 Basic iteration of :
     
     1. Series -> values
     2. DataFrame -> column labels
     3. Panel -> item labels
     

'''

# ================ Iterating DataFrame ========================================

# Iterating a DataFrame gives column names
import pandas as pd
import numpy as np
 
N=20

df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
    'x': np.linspace(0,stop=N-1,num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
    'D': np.random.normal(100, 10, size=(N)).tolist()
    })

for col in df:
   print(col)
   
   
# ================ Tterating over the rows of the DataFrame ===================
   
   '''
   
   1. iteritems() − to iterate over the (key,value) pairs

   2. iterrows() − iterate over the rows as (index,series) pairs

   3. itertuples() − iterate over the rows as namedtuples
   
   '''
   

   
'''============= iteritems() =================================================='''

#Iterates over each column as key, value pair with label as key and column value as a Series object
import pandas as pd
import numpy as np
 
df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
for key,value in df.iteritems():
   print(key,value)
   
'''============= iterrows() =================================================='''

#iterrows() returns the iterator yielding each index value along with a series containing the data in each row
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
for row_index,row in df.iterrows():
   print(row_index,row)   
   
# Note − Because iterrows() iterate over the rows, it doesn't preserve the data 
# type across the row. 0,1,2 are the row indices and col1,col2,col3 are column indices.   
   
   
'''============= itertuples() =================================================='''   
   
# itertuples() method will return an iterator yielding a named tuple for each row
# in the DataFrame. The first element of the tuple will be the row’s corresponding
# index value, while the remaining values are the row values.   


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
for row in df.itertuples():
    print(row)
   
'''

Note − Do not try to modify any object while iterating. Iterating is meant for reading
 and the iterator returns a copy of the original object (a view), thus the changes will
 not reflect on the original object.

'''   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
