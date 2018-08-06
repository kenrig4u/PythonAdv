# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 14:55:08 2018

@author: SilverDoe
"""

'''==== Linear algebra====

SciPy.linalg vs NumPy.linalg
============================
A scipy.linalg contains all the functions that are in numpy.linalg. Additionally, scipy.
linalg also has some other advanced functions that are not in numpy.linalg. Another advantage
of using scipy.linalg over numpy.linalg is that it is always compiled with BLAS/LAPACK support,
while for NumPy this is optional. Therefore, the SciPy version might be faster depending on how 
NumPy was installed.

https://docs.scipy.org/doc/scipy/reference/tutorial/linalg.html
'''
#============= Solving lenear Equations =======================================

#importing the scipy and numpy packages
from scipy import linalg
import numpy as np

#Declaring the numpy arrays
a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])

#Passing the values to the solve function
x = linalg.solve(a, b)

#printing the result array
print(x)

#========== Finding Determinanat ==============================================

#importing the scipy and numpy packages
from scipy import linalg
import numpy as np

#Declaring the numpy array
A = np.array([[1,2],[3,4]])

#Passing the values to the det function
x = linalg.det(A)

#printing the result
print(x)



#======= Finding Eigen values and Eigen vectors ===============================


#importing the scipy and numpy packages
from scipy import linalg
import numpy as np

#Declaring the numpy array
A = np.array([[1,2],[3,4]])

#Passing the values to the eig function
l, v = linalg.eig(A)

#printing the result for eigen values
print(l)

#printing the result for eigen vectors
print(v)



#==================== SVD =====================================================

'''A Singular Value Decomposition (SVD) can be thought of as an extension of the eigenvalue
problem to matrices that are not square.

The scipy.linalg.svd factorizes the matrix ‘a’ into two unitary matrices ‘U’ and ‘Vh’ and a
 1-D array ‘s’ of singular values (real, non-negative) such that a == U*S*Vh, where ‘S’ is a
 suitably shaped matrix of zeros with the main diagonal ‘s’.

'''

#importing the scipy and numpy packages
from scipy import linalg
import numpy as np

#Declaring the numpy array
a = np.random.randn(3, 2) + 1.j*np.random.randn(3, 2)

#Passing the values to the eig function
U, s, Vh = linalg.svd(a)

# printing the result
print(U, Vh, s)


#==============================================================================


















