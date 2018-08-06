# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 21:20:02 2018

@author: SilverDoe
"""

#============== Trignometric functions ========================================
import numpy as np 
a = np.array([0,30,45,60,90]) 
 

rad =a*np.pi/180 # converting to radian

deg = np.degrees(rad) # converting to degrees

# finding trigonmetric ratios
sine = np.sin(rad)
cosine = np.cos(rad)
tangent = np.tan(rad)

print(sine)
print(cosine) 
print(tangent)

# finding inverse
sinv = np.arcsin(sine) 
cinv = np.arccos(cosine)
tinv = np.arctan(tangent)

print(sinv)
print(cinv)
print(tinv)



#============= round, ceil, floor =============================================

import numpy as np 
a = np.array([1.0,5.55, 123, 0.567, 25.532]) 

print(np.around(a)) 
print(np.around(a, decimals = 1)) 
print(np.around(a, decimals = -1))

print(np.floor(a))
print(np.ceil(a))

#============= Arithmetic Operations ==========================================

import numpy as np 

a = np.arange(9, dtype = np.float_).reshape(3,3) 
print('First array:') 
print(a) 
print('\n')  

print('Second array:') 
b = np.array([10,10,10]) 
print(b) 
print('\n')  

print('Add the two arrays:') 
print(np.add(a,b))
print('\n')  

print('Subtract the two arrays:')
print(np.subtract(a,b) )
print('\n')  

print('Multiply the two arrays:') 
print(np.multiply(a,b)) 
print('\n')  

print('Divide the two arrays:') 
print(np.divide(a,b))


#============== reciprocal, power, mod =====================================

# recoprocal
import numpy as np 
a = np.array([1,2,3,4,5],dtype='float') # reciprocal of integers will be zero for any number greater than 1
print(np.reciprocal(a)) 

# power
import numpy as np 
a = np.array([10,100,1000]) 
b = np.array([1,2,3]) 
print(np.power(a,b))

'''import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([2,3,4,5,6])
print(np.power(a,2))
print(a,b)'''

# mod
import numpy as np
a = np.array([10,11,12,13,14,15])
b = np.array([2,3,4,5,6,7])
print(np.mod(a,2))
print(np.mod(a,b)) #np.remainder(a,b) also produces the same result


#============= operation on complex numbers ===================================

import numpy as np 
a = np.array([-5.6j, 0.2j, 11. , 1+1j])

print(np.real(a))
print(np.imag(a))
print(np.conj(a))
print(np.angle(a))
print(np.angle(a, deg = True))



#============ Statistical functions ===========================================

import numpy as np 
a = np.array([[3,7,5],[8,5,3],[2,87,9]]) 
print(a)
# return the minimum from the elements in the given array along the specified axis
print(np.amin(a))
print(np.amin(a, axis=0))
print(np.amin(a, axis=1))

# return the maximum from the elements in the given array along the specified axis
print(np.amax(a))
print(np.amax(a,axis=0))
print(np.amax(a,axis=1))

# ptp() returns the range (maximum-minimum) of values along an axis.
print(np.ptp(a)) # 87-2
print(np.ptp(a,axis=0)) # 8-2, 87-5, 9-3
print(np.ptp(a,axis=1)) # 7-3, 8-3, 87-2



import numpy as np 
a = np.array([[90,91,94],[80,60,93],[70,90,60]]) 
print(a) 

print(np.percentile(a,50))
print(np.percentile(a,50, axis=0))
print(np.percentile(a,50, axis=1))

# defined as the value separating the higher half of a data sample from the lower half
#The median is the 50th percentile: the point in the data where 50% of the data fall below that point, and 50% fall above it.
print(np.median(a))
print(np.median(a, axis=0))
print(np.median(a, axis=1))

print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))

#Weighted average is an average resulting from the multiplication of each component by a factor reflecting its importance.
wts = np.array([4,3,2]) 
print(np.average(a)) # same as mean when no weight is given
print(np.average(a,returned=True))# Returns the sum of weights, if the returned parameter is set to True.
print(np.average(a,weights = wts, axis=0))
print(np.average(a,weights = wts, axis=1))

# mean(abs(x - x.mean())**2)
print(np.var(a))
print(np.var(a, axis=0))
print(np.var(a, axis=1))

# sqrt(mean(abs(x - x.mean())**2))
print(np.std(a))
print(np.std(a, axis=0))
print(np.std(a, axis=1))
























 
 
 
 
 


