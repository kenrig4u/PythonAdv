# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 15:23:58 2018

@author: SilverDoe
"""

from skimage import data, io, filters

image = data.coins()
io.imshow(image)
io.show()
# ... or any other NumPy array!
edges = filters.sobel(image)
io.imshow(edges)
io.show()










