# Inner(inner product) and Outer(outer product)

# ========== Inner =========== 
# The inner tool returns the inner product of two arrays.
''' import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.inner(A, B)     #Output : 4 '''
# ========== Outer  =========== 
# The outer tool returns the outer product of two arrays.
''' import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.outer(A, B)     #Output : [[0 0]
                            #          [3 4]]   '''


# Sample Input
''' 0 1
    2 3 '''
# Sample Output
''' 3
    [[0 0]
    [2 3]] '''

import numpy as np

A = np.array(input().split(), int)
B = np.array(input().split(), int)

print(np.inner(A,B))
print(np.outer(A,B))