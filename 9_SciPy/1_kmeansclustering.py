# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 20:38:39 2018

@author: SilverDoe
"""

'''

>> K-means clustering is a clustering algorithm that aims to partition n observations into k clusters.

There are 3 steps:
    
    1. Initialisation – K initial “means” (centroids) are generated at random.
    2. Assignment – K clusters are created by associating each observation with the nearest centroid.
    3. Update – The centroid of the clusters becomes the new mean.
    
    Assignment and Update are repeated iteratively until convergence.
    The end result is that the sum of squared errors is minimised between points and their respective centroids.
    

'''


from pylab import plot,show
from numpy import vstack,array
from numpy.random import rand
from scipy.cluster.vq import kmeans,vq,whiten

# data generation
data1 = vstack((rand(100,2)+array([.5,.5]),rand(100,2)))
data = whiten(data1)

centroids,_ = kmeans(data,2)

idx,_ = vq(data,centroids)

# some plotting using numpy's logical indexing
plot(data[idx==0,0],data[idx==0,1],'ob',data[idx==1,0],data[idx==1,1],'or')
plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
show()









