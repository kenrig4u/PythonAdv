# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 15:09:37 2018

@author: SilverDoe
"""

'''

Fourier Transformation is computed on a time domain signal to check its behavior in
the frequency domain. Fourier transformation finds its application in disciplines
such as signal and noise processing, image processing, audio signal processing, etc.
SciPy offers the fftpack module, which lets the user compute fast Fourier transforms.

https://docs.scipy.org/doc/scipy/reference/fftpack.html
'''

'''======= One Dimensional Discrete Fourier Transform =========================

The FFT y[k] of length N of the length-N sequence x[n] is calculated by fft() and
the inverse transform is calculated using ifft().


'''

#Importing the fft and inverse fft functions from fftpackage
from scipy.fftpack import fft,ifft
import numpy as np

#create an array with random n numbers
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

#Applying the fft function
y = fft(x)
print(y)

z = ifft(y)
print(z)


'''======== Discrete Cosine Transform =========================================

A Discrete Cosine Transform (DCT) expresses a finite sequence of data points in terms
 of a sum of cosine functions oscillating at different frequencies. SciPy provides a 
 DCT with the function dct and a corresponding IDCT with the function idct.
 
'''

from scipy.fftpack import dct,idct

a =np.array([4., 3., 5., 10., 5., 3.])

disf=  dct(a) 
print(disf)

idisf = idct(disf)
print(idisf)
 

























