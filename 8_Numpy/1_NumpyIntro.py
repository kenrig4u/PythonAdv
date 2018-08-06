# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:41:13 2018

@author: SilverDoe
"""

'''

>> numpy provides n-dimensional array objects(arrays).

>> The ndarray object consists of contiguous one-dimensional segment of computer
 memory, combined with an indexing scheme that maps each item to a location in the memory block.

numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

================= Parameters ==================================================

object : Any object exposing the array interface method returns an array, or any (nested) sequence.

dtype : Desired data type of array, optional.

copy : Optional. By default (true), the object is copied.

order : C (row major) or F (column major) or A (any) (default).

subok : By default, returned array forced to be a base class array. If true, sub-classes passed through.

ndmin : Specifies minimum dimensions of resultant array.

================== Attributes =================================================

1. T	      : Same as self.transpose(), except that self is returned if self.ndim < 2.

2. data	   : Python buffer object pointing to the start of the array’s data.

3. dtype	   : Data-type of the array’s elements.

4. flags	   : Information about the memory layout of the array.

5. flat	   : A 1-D iterator over the array.

6. imag	   : The imaginary part of the array.

7. real	   : The real part of the array.

8. size	   : Number of elements in the array.

9. itemsize	: Length of one array element in bytes.

10. nbytes	: Total bytes consumed by the elements of the array.

11. ndim	   : Number of array dimensions.

12. shape	   : Tuple of array dimensions.

13. strides : Tuple of bytes to step in each dimension when traversing an array.

14. ctypes	: An object to simplify the interaction of the array with the ctypes module.

15. base	   : Base object if memory is from some other object.


'''

#================= creating a 1D array from a list ============================
import numpy as np
list1 = [0,1,2,3,4]
arr1d = np.array(list1)

print(type(arr1d))
print(arr1d)

'''=============== Arrays vs List =============================================

>> Arrays are designed to handle vectorized operations while a python list is not.
   i.e if you apply a function it is performed on every item in the array, rather
   than on the whole array object.
'''
list1 + 2  # error
arr1d + 2
'''
>> Numpy arrays are size immutable. You need to initialize a new array to increase the size.

>> Stores data of the same type. array function automatically promotes all of the numbers
   to the type of the most general entry in the list

>> Numpy arrays can be made value immutable/ write protected.

'''
# making array unwriteable
a = np.arange(10)
a.flags.writeable = True
a.flags['WRITEABLE'] = True
print(a)
a[0] = 1




#=============== Create a 2d array from a list of lists(matrix) ===============
import numpy as np
list2 = [[0,1,2], [3,4,5], [6,7,8]]

# default dtype
arr2d = np.array(list2)
print(arr2d)

# dtype as float
arr2d1 = np.array(list2,dtype='float') #other types : int,str,object,bool,complex,intp,int8 etc
print(arr2d1)
arr2d1.tolist()
arr2d1.tostring()
arr2d1.tobytes()
arr2d1.tofile()




'''==================== Indexing and Slicing =================================='''


# slicing
import numpy as np
data =[
    ('Natsu', 20,'Salamander'),
    ('Lucy', 20,'Princess'),
    ('Erza', 23,'Titania'),
    ('Gray', 23,'Ice Boy'),
    ('Wendy', 12,'Sky Sorceress'),
    ('Jellal', 23,'Mystogan'),]

members = np.array(data)

s = slice(2,4,1) # slice funtion
print(members[s])
print(members[3:]) # slice items starting from index 
print(members[3:5]) # slice items between indexes 
print(members[3:5,1:3])
print(members[1:4,[1,2]])
print(members[...,1]) # returns array of items in the second column 
print(members[3,...]) # slice all items from the 4th row 
print(members[...,1:]) # slice all items from column 1 onwards 

print(members[[0,1,2], [0,1,0]])


rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]]) 
print(members[rows,cols])


# boolean array indexing
list2 = [[0,1,2], [3,34,5], [22,7,8]]
# default dtype
numbers = np.array(list2)
print(numbers[numbers<20]) # works if the dtype is a number


'''======== Omitting NAN values from the output ==============================='''

import numpy as np

data = [np.nan, 1,2,np.nan,3,4,5] 
a = np.array(data) 
print(a[~np.isnan(a)]) # NaN elements are omitted by using ~ (complement operator)

'''======== Filter out complex numbers ===================================='''

import numpy as np 
a = np.array([1, 2+6j, 5, 3.5+5j]) 
print(a[np.iscomplex(a)])



''' Array Broadcasting ======================='''
# broadcasting refers to the ability of NumPy to treat arrays of different shapes during arithmetic operations

# similar arrays
import numpy as np 
l1 = [[1,2,3,4],[2,5,1,7]]
l2 = [[0,1,2,3],[3,5,1,4]]
a = np.array(l1) 
b = np.array(l2) 
c = a + b 
print(c)


# in the case of dissimilar arrays
import numpy as np 
l1 = [[1,2,3,4],[2,5,1,7]]
l2 = [0,1,2,3]
a = np.array(l1) 
b = np.array(l2) 
c = a + b 
print(c)


'''==================== Array Iteration ======================================='''


import numpy as np 
l1 = [[1,2,3,4],[2,5,1,7]]
a = np.array(l1) 
for x in np.nditer(a):
    print(x)
    
# The order of iteration is chosen to match the memory layout of an array, without considering a particular ordering    
for x in np.nditer(a.T): # iterating over transpose
    print(x)

# difference between C and F stype
import numpy as np
l1 = [[1,2,3,4],[2,5,1,7]]
a = np.array(l1) 
print('Original array is:')
print(a)
print('\n')

print('Transpose of the original array is:')
b = a.T
print(b)
print('\n')

print('Sorted in C-style order:')
c = a.copy(order='C')
print(c)
for x in np.nditer(c):
   print(x)

print('\n')

print('Sorted in F-style order:')
c = a.copy(order='F')
print(c)
for x in np.nditer(c):
   print(x)
   
   
# forcing nditer to use either C or F style
import numpy as np
l1 = [[1,2,3,4],[2,5,1,7]]
a = np.array(l1) 
print('Sorted in C-style order:' )
for x in np.nditer(a, order = 'C'): 
   print(x)
print('\n') 

print('Sorted in F-style order:') 
for x in np.nditer(a, order = 'F'): 
   print(x)
   
   
# modifying values 
import numpy as np
l1 = [[1,2,3,4],[2,5,1,7]]
a = np.array(l1) 
for x in np.nditer(a, op_flags=['readwrite']):
   x[...]=2*x
print('Modified array is:')
print(a)
   
   
















