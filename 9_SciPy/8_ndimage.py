# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 15:09:44 2018

@author: SilverDoe
"""

'''

The SciPy ndimage submodule is dedicated to image processing.

1. Input/Output, displaying images
2. Basic manipulations − Cropping, flipping, rotating, etc.
3. Image filtering − De-noising, sharpening, etc.
4. Image segmentation − Labeling pixels corresponding to different objects
5. Classification
6. Feature extraction
7. Registration




'''

from scipy import misc
f = misc.face()
misc.imsave('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\array.jpg', f) # uses the Image module (PIL)

import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()

face = misc.face(gray = False)
face.mean()
face.max()
face.min()

width, height,t = face.shape


# Cropping
crop_face = face[300: - 300, 400: - 400]
import matplotlib.pyplot as plt
plt.imshow(crop_face)
plt.show()



# up <-> down flip
import numpy as np
from scipy import misc
face = misc.face()
flip_ud_face = np.flipud(face)

import matplotlib.pyplot as plt
plt.imshow(flip_ud_face)
plt.show()


# rotation
from scipy import misc,ndimage
face = misc.face()
rotate_face = ndimage.rotate(face, 30)

import matplotlib.pyplot as plt
plt.imshow(rotate_face)
plt.show()



'''==================== Filtering ============================================='''

# blurring
'''
Blurring is widely used to reduce the noise in the image

'''
from scipy import misc,ndimage
face = misc.face()
blurred_face = ndimage.gaussian_filter(face, sigma=1)
import matplotlib.pyplot as plt
plt.imshow(blurred_face)
plt.show()


# edge detection

'''
Edge detection is an image processing technique for finding the boundaries of objects
 within images. It works by detecting discontinuities in brightness. Edge detection is
 used for image segmentation and data extraction in areas such as Image Processing, 
 Computer Vision and Machine Vision.
'''
import scipy.ndimage as nd
import numpy as np

im = np.zeros((256, 256))
im[64:-64, 64:-64] = 1
im[90:-90,90:-90] = 2
im = ndimage.gaussian_filter(im, 8)

import matplotlib.pyplot as plt
plt.imshow(im)
plt.show()

'''
The image looks like a square block of colors. Now, we will detect the edges of those 
colored blocks. Here, ndimage provides a function called Sobel to carry out this operation.
Whereas, NumPy provides the Hypot function to combine the two resultant matrices to one.

'''

import matplotlib.pyplot as plt

im = np.zeros((256, 256))
im[64:-64, 64:-64] = 1
im[90:-90,90:-90] = 2
im = ndimage.gaussian_filter(im, 8)

sx = ndimage.sobel(im, axis = 0, mode = 'constant')
sy = ndimage.sobel(im, axis = 1, mode = 'constant')
sob = np.hypot(sx, sy)

plt.imshow(sob)
plt.show()


'''
The most commonly used edge detection algorithms include

Sobel
Canny
Prewitt
Roberts
Fuzzy Logic methods

'''


