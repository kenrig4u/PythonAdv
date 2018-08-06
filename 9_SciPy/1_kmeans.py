# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 21:30:53 2018

@author: SilverDoe
"""

'''=================== K-means Clustering =====================================

 K-means clustering is a type of unsupervised learning, which is used when you have
 unlabeled data (i.e., data without defined categories or groups). The goal of this
 algorithm is to find groups in the data, with the number of groups represented by
 the variable K. The algorithm works iteratively to assign each data point to one
 of K groups based on the features that are provided. Data points are clustered 
 based on feature similarity. The results of the K-means clustering algorithm 
 are:

     1. The centroids of the K clusters, which can be used to label new data.
     2. Labels for the training data (each data point is assigned to a single cluster)
     
     
     
 K-Means is widely used for many applications.

    >> Image Segmentation
    >> Clustering Gene Segementation Data
    >> News Article Clustering
    >> Clustering Languages
    >> Species Clustering
    >> Anomaly Detection


 Our algorithm works as follows, assuming we have inputs x1,x2,x3,…,xn and value of K

 >> Step 1 - Pick K random points as cluster centers called centroids.
 >> Step 2 - Assign each xi to nearest cluster by calculating its distance to each centroid.
 >> Step 3 - Find new cluster center by taking the average of the assigned points.
 >> Step 4 - Repeat Step 2 and 3 until none of the cluster assignments change.
 '''
 
 '''========== Some numpy functions ==========================================
 
stack       : Join a sequence of arrays along a new axis.
hstack      : Stack arrays in sequence horizontally (column wise).
vstack      : Stack arrays in sequence vertically 
dstack      : Stack arrays in sequence depth wise (along third dimension).
concatenate : Join a sequence of arrays along an existing axis.
vsplit      : Split array into a list of multiple sub-arrays vertically.
block       : Assemble arrays from blocks.
 '''
 import numpy as np
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
np.vstack((a,b))

a = np.array([[1], [2], [3]])
b = np.array([[2], [3], [4]])
np.vstack((a,b))

 
 '''
 scipy.cluster.vq.vq(obs, code_book, check_finite=True)
 ======================================================
 
 Assigns a code from a code book to each observation. Each observation vector in
 the ‘M’ by ‘N’ obs array is compared with the centroids in the code book and assigned
 the code of the closest centroid.
 
1. obs(ndarray) : Each row of the ‘M’ x ‘N’ array is an observation. The columns are 
                  the “features” seen during each observation. The features must be
                  whitened first using the whiten function or something equivalent. 
 
2. code_book(ndarray) : The code book is usually generated using the k-means algorithm. Each row
                        of the array holds a different code, and the columns are the features of
                        the code.
                        
3. check_finite(boolean,optional) : Whether to check that the input matrices contain 
                                    only finite numbers. Disabling may give a performance
                                    gain, but may result in problems(crashes, non-termination)
                                    if the inputs do contain infinities or NaNs. Default: True
    
4. code(ndarray) : A length M array holding the code book index for each observation.

5. dist(ndarray) : The distortion (distance) between the observation and its nearest code.


Returns :
    
    1. A length N array holding the code book index for each observation.
    2. The distortion (distance) between the observation and its nearest code.
 
'''
# Assign codes from a code book to observations
from numpy import array
from scipy.cluster.vq import vq
code_book = array([[1.,1.,1.],[2.,2.,2.]])
features  = array([[  1.9,2.3,1.7],[  1.5,2.5,2.2],[  0.8,0.6,1.7]])
vq(features,code_book)


'''
scipy.cluster.vq.whiten(obs, check_finite=True)
===============================================
Returns the values in obs scaled by the standard deviation of each column.
Normalize a group of observations on a per feature basis.

Before running k-means, it is beneficial to rescale each feature dimension of the
observation set with whitening. Each feature is divided by its standard deviation
across all observations to give it unit variance.

'''

from scipy.cluster.vq import whiten
import numpy as np
features  = np.array([[1.9, 2.3, 1.7],[1.5, 2.5, 2.2],[0.8, 0.6, 1.7,]])
whiten(features)


'''
scipy.cluster.vq.kmeans(obs, k_or_guess, iter=20, thresh=1e-05, check_finite=True)
==================================================================================
Performs k-means on a set of observation vectors forming k clusters.

The k-means algorithm adjusts the centroids until sufficient progress cannot be made,
i.e. the change in distortion since the last iteration is less than some threshold. 
This yields a code book mapping centroids to codes and vice versa.

returns codebook(ndarray) and distortion(float) 

codebook
========
A k by N array of k centroids. The i’th centroid codebook[i] is represented with the
code i. The centroids and codes generated represent the lowest distortion seen, not
necessarily the globally minimal distortion.

distortion
==========
The distortion between the observations passed and the centroids generated.
Distortion is defined as the sum of the squared differences between the observations
and the corresponding centroid.


#end

1. obs

2. k_or_guess(int or ndarray) : The number of centroids to generate. A code is assigned
                                to each centroid, which is also the row index of the 
                                centroid in the code_book matrix generated.The initial k 
                                centroids are chosen by randomly selecting observations 
                                from the observation matrix. Alternatively, passing a k
                                by N array specifies the initial k centroids.
                                
3. iter(int, optional) : The number of times to run k-means, returning the codebook with
                         the lowest distortion. This argument is ignored if initial centroids
                         are specified with an array for the k_or_guess parameter. This parameter
                         does not represent the number of iterations of the k-means algorithm.
                         
4. thresh(float, optional) : Terminates the k-means algorithm if the change in distortion
                             since the last k-means iteration is less than or equal to thresh.

5. check_finite 


'''

import numpy as np
from scipy.cluster.vq import vq, kmeans, whiten
import matplotlib.pyplot as plt
features  = np.array([[ 1.9,2.3],[ 1.5,2.5],[ 0.8,0.6],[ 0.4,1.8],[ 0.1,0.1],[ 0.2,1.8],[ 2.0,0.5],[ 0.3,1.5],[ 1.0,1.0]])
whitened = whiten(features)
book = np.array((whitened[0],whitened[2]))
kmeans(whitened,book)

#==============================================================================
from numpy import random
random.seed((1000,2000))
codes = 3
kmeans(whitened,codes)

#==============================================================================
# Create 50 datapoints in two clusters a and b
pts = 50
a = np.random.multivariate_normal([0, 0], [[4, 1], [1, 4]], size=pts)
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.multivariate_normal.html
b = np.random.multivariate_normal([30, 10],[[10, 2], [2, 1]],size=pts)
features = np.concatenate((a, b))
# Whiten data
whitened = whiten(features)
# Find 2 clusters in the data
codebook, distortion = kmeans(whitened, 2)
# Plot whitened data and cluster centers in red
plt.scatter(whitened[:, 0], whitened[:, 1])
plt.scatter(codebook[:, 0], codebook[:, 1], c='r')
plt.show()















