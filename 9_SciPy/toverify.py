# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 14:35:46 2018

@author: SilverDoe
"""



#=================== Still to verify/correct===================================

import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster.vq import kmeans, kmeans2, whiten

df = pd.read_csv('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\scidata.csv')
print(df.shape)
df.head()

coordinates = df.as_matrix(columns=['V1', 'V2'])
plt.figure(figsize=(10, 6), dpi=100)
plt.scatter(coordinates[:,0], coordinates[:,1], c='c', s=100)
plt.show()



N = len(coordinates)
w = whiten(coordinates)
k = 100
i = 20

cluster_centroids1, distortion = kmeans(w, k, iter=i)
cluster_centroids2, closest_centroids = kmeans2(w, k, iter=i)

plt.figure(figsize=(10, 6), dpi=100)
plt.scatter(cluster_centroids2[:,0], cluster_centroids2[:,1], c='r', s=100)
plt.show()

#==============================================================================
from numpy import vstack,array
from numpy.random import rand
import pandas as pd
from scipy.cluster import vq
from matplotlib import pyplot as plt




# data generation with three features
data = vstack((rand(100,3) + array([.5,.5,.5]),rand(100,3)))
print(data)
print('===================================================')
#The features in obs(observation) should have unit variance, which can be achieved by passing them through the whiten function
data = vq.whiten(data)
print(data)

# computing K-Means with K = 3 (2 clusters)
centroids,_ = vq.kmeans(data,3)
print(centroids)

# assign each sample to a cluster
clx,_ = vq.vq(data,centroids)

# check clusters of observation
print(clx)

plt.figure(figsize=(10, 6), dpi=100)
plt.scatter(centroids[:,0], centroids[:,1], c='r', s=100)
plt.show()


#====================== using sklearn =====================================
# example a
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\scidata.csv')
print(df.shape)
df.head()
# whitening of data
# df = whiten(df)
f1 = df['V1'].values
f2 = df['V2'].values

X=np.matrix(zip(f1,f2))
plt.scatter(f1, f2, c='black', s=7)

kmeans = KMeans(n_clusters=2).fit(X)

kmeans = KMeans(n_clusters=4).fit(X)


# example 1 ===================================================
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

# Importing the dataset
data = pd.read_csv('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\scidata.csv')
print("Input Data and Shape")
print(data.shape)
data.head()

# Getting the values and plotting it
f1 = data['V1'].values
f2 = data['V2'].values
X = np.array(list(zip(f1, f2)))
#plt.scatter(f1, f2, c='black', s=7)
#====

# Number of clusters
kmeans = KMeans(n_clusters=3)
# Fitting the input data
kmeans = kmeans.fit(X)
# Getting the cluster labels
labels = kmeans.predict(X)
# Centroid values
centroids = kmeans.cluster_centers_
print(centroids) # From sci-kit learn

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c='y',s=100)
ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2], marker='*', c='#050505', s=1000)
#====================================================================
# example 2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

plt.rcParams['figure.figsize'] = (16, 9)

# Creating a sample dataset with 4 clusters
X, y = make_blobs(n_samples=800, n_features=3, centers=4)
y
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2])

# Initializing KMeans
kmeans = KMeans(n_clusters=4)
# Fitting with inputs
kmeans = kmeans.fit(X)
# Predicting the clusters
labels = kmeans.predict(X)
# Getting the cluster centers
C = kmeans.cluster_centers_

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y)
ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker='*', c='#050505', s=1000)




