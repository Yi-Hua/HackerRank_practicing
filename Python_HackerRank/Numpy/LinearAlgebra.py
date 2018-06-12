# Linear Algebra

# ========== linalg.det (determinant) ========== 
# The linalg.det tool computes the determinant of an array. 
''' print numpy.linalg.det([[1 , 2], [2, 1]])       #Output : -3.0  '''

# ========== linalg.eig (eigenvalues) ========== 
# The linalg.eig computes the eigenvalues and right eigenvectors of a square array. 
''' vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
    print vals                                      #Output : [ 3. -1.]
    print vecs                                      #Output : [[ 0.70710678 -0.70710678]
                                                    #          [ 0.70710678  0.70710678]]   '''
# ========== linalg.inv (inverse) ========== 
# The linalg.inv tool computes the (multiplicative) inverse of a matrix.
''' print numpy.linalg.inv([[1 , 2], [2, 1]])       #Output : [[-0.33333333  0.66666667]
                                                    #          [ 0.66666667 -0.33333333]]   '''
# Other routines can be found here

# ====================
# Task: You are given a square matrix A with dimensions NxN. Your task is to find the determinant. 
# Sample Input
''' 2
    1.1 1.1
    1.1 1.1 '''
# Sample Output
''' 0.0 '''

import numpy as np

numpy.set_printoptions(legacy='1.13')   #如果設置為字符串“1.13”，則啟用1.13傳統打印模式。

n = int(input())
A = np.array([input().split() for _ in range(n)], float)
print(A)
print(np.linalg.det(A))



