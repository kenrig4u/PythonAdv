# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 15:47:35 2018

@author: SilverDoe
"""

'''
======================== Series Basic Functionality ===========================

1. axes	  :Returns a list of the row axis labels.

2. dtype	  :Returns the dtype of the object.

3. empty   :Returns True if series is empty.

4. ndim	  :Returns the number of dimensions of the underlying data, by definition 1.

5. size	  :Returns the number of elements in the underlying data.

6. values	  :Returns the Series as ndarray.

7. head(n)	  :Returns the first n rows. The default number of elements to display is five

8. tail(n)  :Returns the last n rows. The default number of elements to display is five

'''

import pandas as pd
s = pd.Series(["Natsu","Lisanna","Gray","Lucy","Erza",],index = ['1','2','3','4','5'])
print(s.axes)
print(s.dtype)
print(s.empty)
print(s.ndim)
print(s.size)
print(s.values)
print(s.head(2))
print(s.tail(2))


'''
======================== DataFrame Basic Functionality ========================

1.	T        :Transposes rows and columns.

2.	axes     :Returns a list with the row axis labels and column axis labels as the only members.

3	dtypes   :Returns the dtypes in this object.

4.	empty	   :True if NDFrame is entirely empty [no items]; if any of the axes are of length 0.

5.	ndim	   :Number of axes / array dimensions.

6.	shape	   :Returns a tuple representing the dimensionality of the DataFrame.

7.	size	   :Number of elements in the NDFrame.

8.	values	   :Numpy representation of NDFrame.

9. head() 	:Returns the first n rows.

10. tail()   :Returns last n rows.

'''

import pandas as pd
data = {'Name':['Lisanna', 'Natsu', 'Erza', 'Gray'],'Age':[15,20,23,20]}
df = pd.DataFrame(data)
print(df)
print(df.T)
print(df.axes)
print(df.dtypes)
print(df.empty)
print(df.ndim)
print(df.shape)
print(df.size)
print(df.values)
print(df.tail(2))
print(df.head(2))

















