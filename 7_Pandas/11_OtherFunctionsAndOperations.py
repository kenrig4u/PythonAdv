# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:51:01 2018

@author: SilverDoe
"""


'''====================== Working with text data ================================'''

import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])

print(s.str.lower()) # most of the string operations are applicable once the series is treated as string(str)


'''====================== Statistical functions ===============================

    1. Percentage change : pct_change() # applicable on series, df and panels the same way
    2. Covariance : cov(s) # applised on series
                    cov() # applied on Dataframes
                        
    3. Correlation : corr() # shows the linear relationship between any two array of values (series). 
                            Since df is built of series, it can be used to find the correlation between columns
                    
                    
    4. Data Ranking : rank() # Data Ranking produces ranking for each element in the array of elements. 
                      In case of ties, assigns the mean rank.
                      DataFrame.rank(axis=0, method='average', numeric_only=None, na_option='keep', ascending=True, pct=False)


>> Rank optionally takes a parameter ascending which by default is true

>> Rank supports different tie-breaking methods :
    
    1. average − average rank of tied group

    2. min − lowest rank in the group

    3. max − highest rank in the group

    4. first − ranks assigned in the order they appear in the array
    
'''

import pandas as pd
import numpy as np
s = pd.Series(np.random.np.random.randn(5), index=list('abcde'))

s['d'] = s['b'] # so there's a tie

print(s.rank())


"""'''''''''''''''''''''''''''''More Operations''''''''''''''''''''''''''''''''

1. Window functions
2. Aggregations
3. Missing Data
4. Group by
5. Merging/ Joining
6. Concatenation
7. Data Functionality
8. Time Delta 
9. Categorical Data 
10. visualizations
11. IO tools
12. Sparse Data
13. Caveats and Gotchas

"""




















