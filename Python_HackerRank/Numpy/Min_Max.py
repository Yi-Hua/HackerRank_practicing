# Min and Max

# 
# =========== Min ===========  
# The tool min returns the minimum value along a given axis.
''' import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.min(my_array, axis = 0)         #Output : [1 0]
print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
print numpy.min(my_array, axis = None)      #Output : 0
print numpy.min(my_array)                   #Output : 0 '''
# =========== Max ===========  
# The tool max returns the maximum value along a given axis.
''' import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.max(my_array, axis = 0)         #Output : [4 7]
print numpy.max(my_array, axis = 1)         #Output : [5 7 3 4]
print numpy.max(my_array, axis = None)      #Output : 7
print numpy.max(my_array)                   #Output : 7 '''

# ======================  
# Sample Input
''' 4 2
    2 5
    3 7
    1 3
    4 0 '''
# Sample Output
''' 3   '''
# Explanation
''' The min along axis 1 = [2,3,1,0]
    The max of [2,3,1,0] = 3    '''

import numpy

r,c = map(int, input().split())
mx = numpy.array([input().split() for _ in range(r)], int)
arr = numpy.min(mx, axis = 1)
print(numpy.max(arr))