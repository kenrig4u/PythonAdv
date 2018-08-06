# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 13:57:26 2018

@author: SilverDoe
"""
# creating a numpy array of the image
from PIL import Image as pil
import numpy as np

imgdot = 'E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\images\\dot.png'
imghappy = 'E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\happy.jpg'
myimage = pil.open(imghappy)

iar = np.asarray(myimage) 
print(iar)

# plotting the numpy array using matplotlib
import matplotlib.pyplot as plt

plt.imshow(iar)
plt.show()


