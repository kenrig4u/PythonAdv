# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 15:55:02 2018

@author: SilverDoe
"""

'''

numpy.sort(a, axis, kind, order)

kind    : quicksort, mergesort, heapsort. Default is quicksort

'''

import numpy as np  
a = np.array([[3,7],[9,1]]) 

print(np.sort(a))
print(np.sort(a, axis = 0))


dt = np.dtype([('name', 'S10'),('age', int)]) 
a = np.array([("Jellal",23),("Sam",21),("David", 17), ("Athul",22)], dtype = dt) 
print(np.sort(a, order = 'age'))

# numpy.argsort() function performs an indirect sort on input array.
y = np.argsort(a)
print(y)
print(a[y]) # reconstruct original array in sorted order


# function performs an indirect sort using a sequence of keys
import numpy as np 
nm = ('Jellal','Sam','David','Athul') 
dv = ('f.y.', 's.y.', 's.y.', 'f.y.') 
ind = np.lexsort((dv,nm))
print(ind)


# argmax() and argmin() functions return the indices of maximum and minimum elements respectively along the given axis
import numpy as np 
a = np.array([[30,40,70],[80,20,10],[50,90,60]]) 

print(np.argmax(a))
print(np.argmax(a, axis = 1))
print(np.argmax(a, axis = 0))


# numpy.nonzero() function returns the indices of non-zero elements in the input array
import numpy as np 
a = np.array([[30,40,0],[0,20,10],[57,0,60]])
print(np.nonzero (a))

# where() function returns the indices of elements in an input array where the given condition is satisfied
print(np.where(a > 3))

# extract() function returns the elements satisfying any condition.
condition = np.mod(a,2) == 0 
print(np.extract(condition, a))














