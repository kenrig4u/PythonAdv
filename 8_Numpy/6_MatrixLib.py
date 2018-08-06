# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 12:49:49 2018

@author: SilverDoe
"""

import numpy.matlib 
import numpy as np 

print(np.matlib.empty((2,2))) # create an empty matrix filled with random data

print(np.matlib.zeros((2,2))) # creates a matrix filled with zeros
print(np.matlib.ones((2,2))) # creates a matrix filled with ones
print(np.matlib.eye(n = 3, M = 4, k = 0, dtype = float)) # creates a matrix with diagonal elements as 1's
print(np.matlib.identity(5, dtype = float)) # creates a identity matrix of given size

print(np.matlib.rand(3,3)) # matri filled with random values


i = np.matrix('1,2;3,4') # creating a matrix from a string
print(i) 

j = np.asarray(i) # converting a matrix to an array
print(j)

k = np.asmatrix (j) # converting an array to a matrix
print(k)
