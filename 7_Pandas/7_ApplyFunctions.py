# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 20:51:01 2018

@author: SilverDoe
"""

'''

To Apply our own function or some other library’s function, pandas provide three
 important functions namely :
     
     1. Table wise Function Application: pipe()
     2. Row or Column Wise Function Application: apply()
     3. Element wise Function Application: applymap()
     
>> pipe() function performs the custom operation for the entire dataframe. 
>> apply() function performs the custom operation for either row wise or column wise.
>> applymap() Function performs the specified operation for all the elements of the dataframe.

'''

''' ============== pipe() function ============================================'''

# pipe() Function to add value 2 to the entire dataframe
import pandas as pd
 

def adder(adder1,adder2):
   return adder1+adder2
 
#Create a Dictionary of series
d = {'Score_Math':pd.Series([66,57,75,44,31,67,85,33,42,62,51,47]),
   'Score_Science':pd.Series([89,87,67,55,47,72,76,79,44,92,93,69])}
 
df = pd.DataFrame(d)
print(df)
print(df.pipe(adder,2))


''' ============== apply() function ==========================================='''

# apply() Function to find the mean of values across rows and mean of values across columns
import pandas as pd
import numpy as np 
 
#Create a DataFrame
d = {'Score_Math':pd.Series([66,57,75,44,31,67,85,33,42,62,51,47]),
   'Score_Science':pd.Series([89,87,67,55,47,72,76,79,44,92,93,69])}
 
df = pd.DataFrame(d)
print(df) 

print(df.apply(np.mean)) # by default column wise
print(df.apply(np.mean,axis=0)) # column-wise/across rows
print(df.apply(np.mean,axis=1)) # row-wise/across columns


''' ============= applymap() =================================================='''


import pandas as pd
import math
 
 #Create a DataFrame
d = {'Score_Math':pd.Series([66,57,75,44,31,67,85,33,42,62,51,47]),
   'Score_Science':pd.Series([89,87,67,55,47,72,76,79,44,92,93,69])}
 
df = pd.DataFrame(d)
print(df) 

# multiplying the all the elements of dataframe by 2 
print(df.applymap(lambda x:x*2))

# finding the square root of all the elements of dataframe with applymap() 
print(df.applymap(lambda x:math.sqrt(x)))




'''==================== More Examples ========================================='''
#1 ===============
import pandas as pd
 
 #Create a DataFrame
d = {'Score_Math':pd.Series([66,57,75,44,31,67,85,33,42,62,51,47]),
   'Score_Science':pd.Series([89,87,67,55,47,72,76,79,44,92,93,69])}
 
df = pd.DataFrame(d)
print(df)

df.apply(lambda x: x.max() - x.min())
print(df.apply(np.mean))

#2 ===============
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])

# My custom function
df['col1'].map(lambda x:x*100)
print(df.apply(np.mean))

#3 ================
import pandas as pd
import numpy as np

# My custom function
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.applymap(lambda x:x*100)
print(df.apply(np.mean))




























