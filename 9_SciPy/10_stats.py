# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 09:52:59 2018

@author: SilverDoe
"""

'''

All of the statistics functions are located in the sub-package scipy.stats and a fairly
complete listing of these functions can be obtained using info(stats) function.

A list of random variables available can also be obtained from the docstring for the
stats sub-package. This module contains a large number of probability distributions
as well as a growing library of statistical functions.

https://docs.scipy.org/doc/scipy/reference/stats.html

'''


'''

A probability distribution in which the random variable X can take any value is continuous
random variable. The location (loc) keyword specifies the mean. The scale (scale) keyword 
specifies the standard deviation.

'''
#================== Normal and Uniform distribution ===========================
from PIL import Image as pil
im = pil.open('E:\\Documents\\SourceCodes\\Python Advanced\\9_SciPy\\distribution.PNG')
im.show()

'''

The cumulative distribution function (CDF, also cumulative density function) of a 
real-valued random variable X, or just distribution function of X, evaluated at x,
is the probability that X will take a value less than or equal to x.

'''

'''================ Normal Distribution =======================================

A normal distribution can be generated using the norm function

'''

#====================== Finding CDF ===========================================

from scipy.stats import norm
import numpy as np

x = np.array([1,-1., 0, 1, 3, 4, -2, 6])
cdfval = norm.cdf(x)
print(cdfval)


'''

To find the median of a distribution, we can use the Percent Point Function (PPF), which
is the inverse of the CDF.
 
'''
#================= Finding PPF ================================================

from scipy.stats import norm
print(norm.ppf(cdfval))


'''

probability density function (PDF), or density of a continuous random variable, is a function,
whose value at any given sample (or point) in the sample space (the set of possible values taken
by the random variable) can be interpreted as providing a relative likelihood that the value of
the random variable would equal that sample

'''
#================= Finding PDF ================================================

from scipy.stats import norm
import numpy as np
x = np.array([1,-1., 0, 1, 3, 4, -2, 6])
print(norm.pdf(x))


#====================== generating random variables ===========================
from scipy.stats import norm
print(norm.rvs(size = 5)) 




'''============= Uniform Distribution =========================================

A uniform distribution can be generated using the uniform function

'''

from scipy.stats import uniform
print (uniform.cdf([0, 1, 2, 3, 4, 5], loc = 1, scale = 4))


'''============= Binomial Distribution =========================================

A binomial distribution can be generated using the binom function

'''
from scipy.stats import binom
print(binom.cdf([0, 1, 2, 3, 4, 5], loc = 1, scale = 4))



