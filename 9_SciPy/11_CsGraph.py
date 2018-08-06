# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 14:57:32 2018

@author: SilverDoe
"""

'''

CSGraph stands for Compressed Sparse Graph, which focuses on Fast graph algorithms based
on sparse matrix representations. A graph is just a collection of nodes, which have links
between them. Graphs can represent nearly anything − social network connections, where 
each node is a person and is connected to acquaintances; images, where each node is a 
pixel and is connected to neighboring pixels; points in a high-dimensional distribution, 
where each node is connected to its nearest neighbors; and practically anything else you can imagine.


One very efficient way to represent graph data is in a sparse matrix: let us call it G.
The matrix G is of size N x N, and G[i, j] gives the value of the connection between 
node ‘i' and node ‘j’. A sparse graph contains mostly zeros − that is, most nodes 
have only a few connections.

The creation of the sparse graph submodule was motivated by several algorithms used in
 scikit-learn that included the following :
     
     1. Isomap − A manifold learning algorithm, which requires finding the shortest paths in a graph.
     
     2. Hierarchical clustering − A clustering algorithm based on a minimum spanning tree.
     
     3. Spectral Decomposition − A projection algorithm based on sparse graph laplacians.
     
     


'''

from PIL import Image as pil
im = pil.open('E:\\Documents\\SourceCodes\\Python Advanced\\9_SciPy\\csgraph.PNG')
im.show()

#==================== sparsed, dense and masked representations
import numpy as np

G_dense = np.array([ [0, 2, 1],
                     [2, 0, 0],
                     [1, 0, 0] ])
                     
G_masked = np.ma.masked_values(G_dense, 0)
from scipy.sparse import csr_matrix

G_sparse = csr_matrix(G_dense)
print(G_sparse.data)

from scipy.sparse.csgraph import csgraph_from_dense
G2_data = np.array
([
   [np.inf, 2, 0 ],
   [2, np.inf, np.inf],
   [0, np.inf, np.inf]
])
G2_sparse = csgraph_from_dense(G2_data, null_value=np.inf)
print(G2_sparse.data)



'''======================= Word ladders using sparse graphs ===================

APE → APT → AIT → BIT → BIG → BAG → MAG → MAN
'''
import numpy as np
from scipy.sparse import csgraph

csgraph.__all__

f_in = open('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\words_alpha.txt','r')
words = f_in.read().split()


words = filter(lambda w: len(w) == 3, words) # keep 3-letter words
words = filter(str.isalpha, words) # no punctuation
words = filter(str.islower, words) # no proper nouns or acronyms

wordlist = list(words)
wordarray = np.sort(wordlist)
wordarray.shape
print(wordarray)

wordarray.size
wordarray.itemsize
wordarray


word_bytes = np.ndarray((wordarray.size, wordarray.itemsize),
                        dtype='int8',
                        buffer=wordarray.data)
word_bytes.shape
word_bytes
type(wordarray.data)

from scipy.spatial.distance import pdist, squareform
from scipy.sparse import csr_matrix
hamming_dist = pdist(word_bytes, metric = 'hamming')
hamming_dist

len(hamming_dist)

# https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.spatial.distance.squareform.html
sqfmdismat = squareform(hamming_dist < 1.5 / wordarray.itemsize)
graph = csr_matrix(sqfmdismat)# compressed sparse matrix

graph
'''

Matrices that contain mostly zero values are called sparse, distinct from matrices where
most of the values are non-zero, called dense.

'''

i1 = wordarray.searchsorted('ape')
i2 = wordarray.searchsorted('man')
i1
i2
print(wordarray[i1],wordarray[i2])

from scipy.sparse.csgraph import dijkstra
distances, predecessors = dijkstra(graph, indices = i1, return_predecessors = True)
print(distances[i2])
print(predecessors[i2])
print(wordarray[predecessors[i2]])
'''
dijkstra algorithm  finds the shortest path in a graph.
======================================================
distances : The matrix of distances between graph nodes. dist_matrix[i,j] gives the shortest 
distance from point i to point j along the graph.

predecessors : The matrix of predecessors, which can be used to reconstruct the shortest paths. 
Row i of the predecessor matrix contains information on the shortest paths from point i: each 
entry predecessors[i, j] gives the index of the previous node in the path from point i to point
 j. If no path exists between point i and j, then predecessors[i, j] = -9999.

'''

path = []
i = i2

while i != i1:
   path.append(wordarray[i])
   i = predecessors[i]
   
path.append(wordarray[i1])
print(path)


