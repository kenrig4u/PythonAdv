# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:28:16 2018

@author: SilverDoe
"""

'''
A panel is a 3D container of data. The term Panel data is derived from econometrics
 and is partially responsible for the name pandas − pan(el)-da(ta)-s.
 
 Axes's involved in panel and their semantic meaning :
     
     1. items - axis 0, each item corresponds to a DataFrame contained inside.
     2. major_axis − axis 1, it is the index (rows) of each of the DataFrames.
     3. minor_axis − axis 2, it is the columns of each of the DataFrames.
     

 pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)
 
 Parameters :
 ============
 
 1. data : Data takes various forms like ndarray, series, map, lists, dict, constants and also another DataFrame
 
 2. items : 	axis=0.
 
 3. major_axis : axis=1.
 
 4. minor_axis : axis=2.
 
 5. dtype	 : Data type of each column.
 
 6. copy : Copy data. Default, false.
 
'''

#========== Empty Panel =======================================================

#creating an empty panel
import pandas as pd
p = pd.Panel()
print(p)

#========== panel from 3D ndarray =============================================

import pandas as pd
import numpy as np

data = np.random.rand(2,4,5)
p = pd.Panel(data)
print(p)

#========== From dictionary to Dataframe objects ==============================

import pandas as pd
import numpy as np

data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p)

#========== Selecting the Data from Panel =====================================

# using items
import pandas as pd
import numpy as np
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p['Item1'])

# Using major_axis
import pandas as pd
import numpy as np
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p.major_xs(1))

# Using minor_axis
import pandas as pd
import numpy as np
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p.minor_xs(1))




































