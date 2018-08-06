# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 21:53:31 2018

@author: SilverDoe
"""

#============== Save numpy array ==============================================
import numpy as np 
a = np.array([1,2,3,4,5]) 
np.save('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\myarray',a)


#============== Load numpy array ==============================================
import numpy as np 
b = np.load('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\myarray.npy') 
print(b) 

#=============

import numpy as np 

a = np.array([1,2,3,4,5,99]) 
np.savetxt('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\myarray2.txt',a) 
b = np.loadtxt('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\myarray2.txt') 
print(b)