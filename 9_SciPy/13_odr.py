# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 22:26:41 2018

@author: SilverDoe
"""

'''
Regression analysis is a technique used to analyze data consisting of a dependent variable (or response
variable) and one or more independent variables (or explanatory variables). The dependent variable is
modeled as a function of independent variables, fixed coefficients known as parameters and an error term.
The error term represents unexplained variation in the dependent variable and is treated as a random
variable. The parameter values are estimated to provide the ”best fit” to the data. The most commonly
used method to estimate parameter values is least squares, where parameter values are chosen to minimize
the squared difference between the true and fitted values summed over all observations.

ODR stands for Orthogonal Distance Regression, which is used in the regression studies. Basic linear 
regression is often used to estimate the relationship between the two variables y and x by drawing the 
line of best fit on the graph.

The mathematical method that is used for this is known as Least Squares, and aims to minimize the sum 
of the squared error for each point. The key question here is how do you calculate the error (also known
as the residual) for each point?

In a standard linear regression, the aim is to predict the Y value from the X value – so the sensible 
thing to do is to calculate the error in the Y values (shown as the gray lines in the following image). 
However, sometimes it is more sensible to take into account the error in both X and Y (as shown by the 
dotted red lines in the following image).

                      
For example − When you know your measurements of X are uncertain, or when you do not want to focus on 
the errors of one variable over another.
'''

from PIL import Image as pil
filename = 'E:\\Documents\\SourceCodes\\Python Advanced\\9_SciPy\\orthogonal_distance_linear_regression.jpg'
im = pil.open(filename)
im.show()

'''

Orthogonal Distance Regression (ODR) is a method that can do this (orthogonal in this context means perpendicular
– so it calculates errors perpendicular to the line, rather than just ‘vertically’).

'''


'''======================== Univariate Regression =============================

# univariate regression or a model with one independent variable.

'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.odr import Model, RealData, ODR
import random

# Initiate some data, giving some randomness using random.random().
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([i**2 + random.random() for i in x])

# Define a function (quadratic in our case) to fit the data with.
def linear_func(p, x):
   m, c = p
   return m*x + c

# Create a model for fitting.
linear_model = Model(linear_func)

# Create a RealData object using our initiated data from above.
data = RealData(x, y)

# Set up ODR with the model and data.
odr = ODR(data, linear_model, beta0=[0., 1.])

# Run the regression.
out = odr.run()

# Use the in-built pprint method to give us results.
out.pprint() # pretty print

slope = out.beta[0]
intercept = out.beta[1]

# xx holds the x limits of the line to draw.  The graph is a straight line,
# so we only need the endpoints to draw it.
xx = np.array([0, 6])  
yy = linear_func(out.beta, xx)
plt.plot(x,y,'ro')
plt.plot(xx, yy,'b')



























