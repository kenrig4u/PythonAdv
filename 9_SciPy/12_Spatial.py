# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 16:35:22 2018

@author: SilverDoe
"""

'''

The scipy.spatial package can compute Triangulations, Voronoi Diagrams and Convex Hulls of
a set of points, by leveraging the Qhull library. Moreover, it contains KDTree implementations
for nearest-neighbor point queries and utilities for distance computations in various metrics.
 
'''


'''======================= Delaunay Triangulations ============================

In mathematics and computational geometry, a Delaunay triangulation for a given set P of 
discrete points in a plane is a triangulation DT(P) such that no point in P is inside the
circumcircle of any triangle in DT(P).

'''
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Delaunay

points = np.array([[0, 4], [2, 1.1], [1, 3], [1, 2]])
tri = Delaunay(points)

tri.points
tri.convex_hull

plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
plt.plot(points[:,0], points[:,1], 'o')
plt.show()

#=================== finding coplanar points =================================
from scipy.spatial import Delaunay
points = np.array([[0, 0], [0, 1], [1, 0], [1, 1], [1, 1]])
tri = Delaunay(points)
print(tri.coplanar)



'''==================== Convex Hulls ==========================================

In mathematics, the convex hull or convex envelope of a set of points X in the Euclidean plane
or in a Euclidean space (or, more generally, in an affine space over the reals) is the smallest
convex set that contains X.

'''
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
points = np.random.rand(10, 2) # 30 random points in 2-D
hull = ConvexHull(points)

plt.plot(points[:,0], points[:,1], 'o')
for simplex in hull.simplices:
    plt.plot(points[simplex,0], points[simplex,1], 'k-')
plt.show()


'''

>> The conventional 2D or 3D (or for that matter nD) space that we regularly use is called the Euclidean space,
   also called the flat space.

>> Why is it called so? Because all the classical laws of geometry that we are aware of (Pythagoras theorem, 
   properties of polygons, etc.) are only valid (in the way we know them) in flat spaces. What it means is 
   that that the line joining any two points in this space is straight.

>> Imagine your computer screen. Draw two points anywhere on it (key : ‘Imagine’). Now the shortest way of 
   reaching one point from the other is a straight line, because this space is flat.

>> Now imagine those two points on the surface of a basketball. For simplicity, on diametrically opposite 
   ends (on poles, if you prefer it). There are infinite ways to reach one point from the other, but the 
   shortest is the semicircle that connects the points; since this ‘space’ is curved. Obviously, the 
   Pythagorean theorem wouldn’t work here (since no straight lines connecting three non-linear points).

>> Therefore this concept of flat space as opposed to curved space exists. And the flat space is conventionally 
   called the Euclidean space because all of Euclidean geometry was done in flat space.
   
'''





























