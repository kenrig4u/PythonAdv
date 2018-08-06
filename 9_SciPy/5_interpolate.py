# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 11:33:31 2018

@author: SilverDoe
"""

'''
Interpolation is the process of finding a value between two points on a line or a curve.

Interpolation is guessing data points that fall within the range of the data you have, i.e.
between your existing data points. Extrapolation is guessing data points from beyond the range of your data set.

https://docs.scipy.org/doc/scipy-1.1.0/reference/interpolate.html
'''

'''================ numpy interpolation =======================================

>> While numpy returns an array with discrete datapoints, 'interp1d' returns a function.
   You can use the generated function later in your code as often as you want.

>> Numpy.interp does not handle complex-valued data or ndim>1, while scipy.interp1d does both.
   OTOH, numpy's interpolator is much faster
'''

# numpy interpolation
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 10)
y = np.sin(x)
xvals = np.linspace(0, 2*np.pi, 50)
yinterp = np.interp(xvals, x, y)
plt.plot(x, y, 'o')
plt.plot(xvals, yinterp, '-x')
plt.show()


#=============================== scipy interp1d ===============================
# scipy interp1d
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
x = np.linspace(0, 4, 12)
y = np.cos(x**2/3+4)

plt.plot(x, y,'o')
plt.show()

f1 = interpolate.interp1d(x, y,kind = 'linear')
f2 = interpolate.interp1d(x, y, kind = 'cubic')

xnew = np.linspace(0, 4,30)
plt.plot(x, y, 'o', xnew, f1(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic'], loc = 'best')
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html
plt.show()

#====================== UnivariateSpline ======================================

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
x = np.linspace(0, 4, 12)
y = np.cos(x**2/3+4)
plt.plot(x, y,'o')
plt.show()


spl = interpolate.UnivariateSpline(x, y)
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.UnivariateSpline.html
xs = np.linspace(0, 4, 1000)
plt.plot(xs, spl(xs), 'g', lw = 3)
plt.show()

# example 2 =================

import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
x = np.linspace(-3, 3, 50)
y = np.exp(-x**2) + 0.1 * np.random.randn(50)
plt.plot(x, y, 'ro', ms = 5)
plt.show()

spl = UnivariateSpline(x, y)
xs = np.linspace(-3, 3, 1000)
plt.plot(xs, spl(xs), 'g', lw = 3)
plt.show()

# manually set smoothing factor
spl.set_smoothing_factor(0.5)
plt.plot(xs, spl(xs), 'b', lw = 3)
plt.show()

# exampe 3 ================


























