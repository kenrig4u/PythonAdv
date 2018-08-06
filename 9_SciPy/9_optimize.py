# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 21:42:00 2018

@author: SilverDoe
"""

'''

Optimization deals with selecting the best option among a number of possible choices
that are feasible or don't violate constraints. Python can be used to optimize parameters
in a model to best fit data, increase profitability of a potential engineering design, or
meet some other type of objective that can be described mathematically with variables and equations.

Mathematical optimization problems may include equality constraints (e.g. =), inequality
constraints (e.g. <, <=, >, >=), objective functions, algebraic equations, differential
equations, continuous variables, discrete or integer variables, etc

https://docs.scipy.org/doc/scipy-1.0.0/reference/generated/scipy.optimize.minimize.html

example of an optimization problem from a benchmark test set is the Hock Schittkowski problem :
    
'''

from PIL import Image as pil
im = pil.open('E:\Documents\SourceCodes\Python Advanced\9_SciPy\ineq.PNG')
im.show()

#==============================================================================

from scipy.optimize import minimize

def objective(x):
    x1 = x[0]
    x2 = x[1] 
    x3 = x[2]
    x4 = x[3]
    return x1*x4*(x1+x2+x3)+x3

def constraint1(x):
    return x[0]*x[1]*x[2]*x[3]-25.0

def constraint2(x):
    sum_sq = 40
    for i in range(4):
        sum_sq = sum_sq-x[i]**2
    return sum_sq


x0 = [1,5,5,1]
print(objective(x0))

b =(1.0,5.0)
bnds = (b,b,b,b)
con1 = {'type':'ineq', 'fun':constraint1}
con2 = {'type':'eq', 'fun':constraint2}
cons = [con1,con2]

sol = minimize(objective,x0,method='SLSQP', bounds=bnds,constraints=cons)
print(sol)
print(sol.x)




'''=============== Finding the root of a vector function ======================

Finding a root of a set of non-linear equations can be achieved using the root() function.
Several methods are available, amongst which hybr (the default) and lm, respectively use
the hybrid method of Powell and the Levenberg-Marquardt method from the MINPACK.


https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root.html
'''

import numpy as np
from scipy.optimize import root
def func(x):
   return x*2 + 2 * np.cos(x)
sol = root(func, 0.3)
print(sol)




'''=================== Least Squares ==========================================

used to determine a line of best fit by minimizing the sum of squares created by a mathematical function.

LSM is used to ﬁt functions to a set of data.

A cost function is a mathematical formula used to used to chart how production expenses
will change at different output levels. In other words, it estimates the total cost of
production given a specific quantity produced.

http://nptel.ac.in/courses/122104019/numerical-analysis/Rathish-kumar/least-square/r1.htm

'''

#Rosenbrock Function
from scipy.optimize import least_squares
import numpy as np
def residual(x):
   return np.array([10 * (x[1] - x[0]**2), (1 - x[0])])
   

inp = np.array([2, 2])
res = least_squares(residual, inp)

print(res)




















