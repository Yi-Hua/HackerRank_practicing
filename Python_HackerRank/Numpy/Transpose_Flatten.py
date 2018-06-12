# Transpose and Flatten
''' array.transpose()
    array.flatten()     '''
# Input : The first line contains the space separated values of N and M. 
#         The next N lines contains the space separated elements of M columns.
''' 2 2      #2X2 matrix
    1 2
    3 4 '''
# Output : First, print the transpose array and then print the flatten.
''' [[1 3]
    [2 4]]
    [1 2 3 4]   '''

import numpy

n, m = map(int, input().split())                                        # size : NxM
array = numpy.array([input().strip().split() for _ in range(n)], int)
print (array.transpose())
print (array.flatten())

# ==================================================================================
# Transpose 矩陣轉置
''' #We can generate the transposition of an array using the tool numpy.transpose. 
    #It will not affect the original array, but it will create a new array.
import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print numpy.transpose(my_array)

#Output
[[1 4]
 [2 5]
 [3 6]] '''
# Flatten 拉成向量====================================================================
''' #The tool flatten creates a copy of the input array flattened to one dimension.
import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print my_array.flatten()

#Output
[1 2 3 4 5 6]   '''