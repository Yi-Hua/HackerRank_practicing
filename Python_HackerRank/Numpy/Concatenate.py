# Concatenate 連環 : Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined:
''' numpy.concatenate((arrA, arrB), axis = 0))'''  # axis = 0 : 鉛直方向
# Input          # first line : matrix size (4+3)X2
''' 4 3 2        # matrix size: (a+b)xc
    1 2
    1 2 
    1 2
    1 2
    3 4
    3 4
    3 4     '''
# Output
''' [[1 2]
    [1 2]
    [1 2]
    [1 2]
    [3 4]
    [3 4]
    [3 4]] '''

import numpy as np
a, b, c = map(int,input().split())  # matrix size: (a+b)xc

arrA = np.array([input().split() for _ in range(a)],int)    # [[1 2]
#print(arrA)                                                #  [1 2]                                                          
                                                            #  [1 2]
                                                            #  [1 2]]
arrB = np.array([input().split() for _ in range(b)],int)                                                             
#print(arrB)                                                 # [[3 4]
                                                            #  [3 4]
                                                            #  [3 4]]
print(np.concatenate((arrA, arrB), axis = 1))   # axis = 0 : 鉛直方向
                                                # axis = 1 : 水平方向       

# =======================================================================================
#ex 1
''' import numpy
array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print numpy.concatenate((array_1, array_2, array_3))    

#Output
[1 2 3 4 5 6 7 8 9] '''
#ex 2
''' import numpy
array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print(numpy.concatenate((array_1, array_2), axis = 1))   

#Output
[[1 2 3 0 0 0]
 [0 0 0 7 8 9]]   '''