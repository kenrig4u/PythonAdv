# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 00:41:37 2018

@author: SilverDoe
"""

'''====================== Image IO ============================================
The purpose of imageio is to support reading and writing of image data. We're not processing images,
you should use e.g. scikit-image for that.

https://imageio.github.io/
http://imageio.readthedocs.io/en/latest/examples.html#iterate-over-frames-in-a-movie
'''
# read a local image
import imageio
im = imageio.imread('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\happy.jpg')
im.shape  # im is a numpy array
imageio.imwrite('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\imageiohappy.jpg', im[355:, :, 2])


# read from the internet
import imageio
import visvis as vv

img = imageio.imread('http://upload.wikimedia.org/wikipedia/commons/d/de/Wikipedia_Logo_1.0.png')
img.shape
vv.imshow(img)
#imageio.imwrite('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\inter.jpg', img[:, :])

# Iterate over frames in a movie
import imageio

reader = imageio.get_reader('D:\\Videos\\Movies\\Hollywood\\Before I Wake (2016) [YTS.AG]\\Before.I.Wake.2016.720p.BluRay.x264-[YTS.AG].mp4')
for i, im in enumerate(reader):
    print('Mean of frame %i is %1.1f' % (i, im.mean()))

# Grab screenshot or image from the clipboard
import imageio

im_screen = imageio.imread('<screen>')
im_clipboard = imageio.imread('<clipboard>')


# Grab frames from your webcam
import imageio
import visvis as vv

reader = imageio.get_reader('<video0>')
t = vv.imshow(reader.get_next_data(), clim=(0, 255))
for im in reader:
    vv.processEvents()
    t.SetData(im)