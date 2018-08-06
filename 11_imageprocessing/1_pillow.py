# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 22:23:44 2018

@author: SilverDoe
"""
'''

The Python Imaging Library (PIL) was developed for Python 2.x and provided functions
to manipulate images, including reading, modifying and saving in various standard image
formats in a package called "PIL". With the coming of age of Python 3.x, a fork of the 
older version has evolved that is more suited for the new technologies and is in a package called "Pillow".


https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
http://pillow.readthedocs.io/en/3.1.x/handbook/tutorial.html
'''

# Rotate image
from PIL import Image as pil

myimage = pil.open('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\happy.jpg')
myimage.format
myimage.size
myimage.mode
mirror = myimage.transpose(pil.ROTATE_270)

mirror.save('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\behappy.jpg')


# Image Filter Blur an Image
from PIL import Image, ImageFilter

original = Image.open('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\happy.jpg')
blurred = original.filter(ImageFilter.BLUR)
original.show()
blurred.show()


# Creating Thumbnails
from PIL import Image, ImageFilter
original = Image.open('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\happy.jpg')
original.thumbnail((128,128))
original.show()


# resize an image
from PIL import Image, ImageFilter
image = Image.open('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\happy.jpg')
image = image.resize((1600, 900), Image.LANCZOS)
image.show()


# crop an image
from PIL import Image, ImageFilter

original = Image.open('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\happy.jpg')
width, height = original.size   # Get dimensions
left = width/4
top = height/4
right = 3 * width/4
bottom = 3 * height/4
croppedimg = original.crop((left, top, right, bottom))
croppedimg.show()






