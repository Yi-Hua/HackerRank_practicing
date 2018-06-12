# Sum and Prod(product)

# ========== sum ========== 
# numpy.sum():The sum tool returns the sum of array elements over a given axis. 
''' import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])                          #  1  2  | 3
                                                                    #  3  4  | 7
print numpy.sum(my_array, axis = 0)         #Output : [4 6]         #  _  _
print numpy.sum(my_array, axis = 1)         #Output : [3 7]         #  4  6
print numpy.sum(my_array, axis = None)      #Output : 10
print numpy.sum(my_array)                   #Output : 10    '''
# ========== prod ========== 
# numpy.prod():The prod tool returns the product of array elements over a given axis. 
''' import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])                          #  1  2  | 2
                                                                    #  3  4  | 12
print(numpy.prod(my_array, axis = 0))            #Output : [3 8]     #  _  _
print(numpy.prod(my_array, axis = 1))            #Output : [2 12]    #  3  8
print(numpy.prod(my_array, axis = None))         #Output : 24
print(numpy.prod(my_array))                      #Output : 24    '''
# ====================
# Sample Input
''' 2 2
    1 2
    3 4 '''
# Sample Output
'''  24  '''

import numpy

r ,c  = map(int, input().split())
mx = numpy.array([input().split() for _ in range(r)],int)
arr = numpy.sum(mx, axis = 0)
print(numpy.prod(arr)) 

