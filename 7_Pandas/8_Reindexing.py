# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 13:59:16 2018

@author: SilverDoe
"""

''' Reindexing changes the row labels and column labels of a DataFrame. To reindex means to conform the data to match a given set of labels along a particular axis.
        
        Options that can be accomplished through reindexing :
            
            1. Reorder the existing data to match a new set of labels.
            2. Insert missing value (NA) markers in label locations where no data for the label existed.

'''


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

#reindex the DataFrame
df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])

print(df_reindexed)

#======================== Reindex to Align with Other Objects ================

#You may wish to take an object and reindex its axes to be labeled the same as another object
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])

df1 = df1.reindex_like(df2)
print(df1)



#==================== Filling while ReIndexing ================================

import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])

# Padding NAN's
print(df2.reindex_like(df1))

# Now Fill the NAN's with preceding Values
print ("Data Frame with Forward Fill:")
print(df2.reindex_like(df1,method='ffill'))

#======================== Limits on Filling while Reindexing ==================

#The limit argument provides additional control over filling while reindexing. 
#Limit specifies the maximum count of consecutive matches
import pandas as pd
import numpy as np
 
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])

# Padding NAN's
print(df2.reindex_like(df1))

# Now Fill the NAN's with preceding Values
print("Data Frame with Forward Fill limiting to 1:")
print(df2.reindex_like(df1,method='ffill',limit=1))

#========================= Renaming ==================================
#The rename() method allows you to relabel an axis based on some mapping (a dict or Series) or an arbitrary function.
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print(df1)

print("After renaming the rows and columns:")
print(df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'},
index = {0 : 'apple', 1 : 'banana', 2 : 'durian'}))

















