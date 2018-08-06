# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 22:56:27 2018

@author: SilverDoe
"""


'''=============== Linear Regression =========================================='''

import matplotlib.pyplot as plt 
from sklearn import linear_model # contains linear regression module

height = [[1.47], [1.50], [1.52], [1.55], [1.57], [1.60], [1.63], [1.65], [1.68], [1.70], [1.73], [1.75], [1.78], [1.80], [1.83]]
mass = [52.21, 53.12, 54.48, 55.84, 57.20, 58.57, 59.93, 61.29, 63.11, 64.47, 66.28, 68.10, 69.92, 72.19, 74.46]

reg = linear_model.LinearRegression() # our regression module
reg.fit(height, mass) # make it learn the data

a = reg.coef_[0] # the a value is stored as coefficient
b = reg.intercept_ # the b value is stored as intercept

ablineValues = [] # this list stores the predicted value for all points
for i in height:
    ablineValues.append(a * i[0] + b)
 
plt.scatter(height, mass) # plot the points
plt.plot(height, ablineValues, 'r') # plot the line
plt.show() # show the plot










