# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 13:41:32 2018

@author: SilverDoe
"""

'''
SciPy has many modules, classes, and functions available to read data from and write data to a variety of file formats.

https://docs.scipy.org/doc/scipy/reference/io.html
'''

import scipy.io as sio
import numpy as np

#Save a mat file
vect = np.arange(10)
print(vect)
sio.savemat('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\array.mat', {'vect':vect})

#Now Load the File
mat_file_content = sio.loadmat('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\array.mat')
print(mat_file_content)


mat_file_content = sio.whosmat('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\array.mat')
print(mat_file_content)