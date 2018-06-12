#Shape and Reshape

# Input : A single line of input containing 9 space separated integers.
''' 1 2 3 4 5 6 7 8 9   '''
# Output : Print the 3X3 NumPy array.
''' [[1 2 3]
    [4 5 6]
    [7 8 9]]    '''
import numpy
                                        # 1 2 3 4 5 6 7 8 9
list = list(map(int,input().split()))   #[1,2,3,4,5,6,7,8,9]

# code 1 ---------------------------------------------------------
# my_array = numpy.array(list)            #[1 2 3 4 5 6 7 8 9]
# print(numpy.reshape(my_array,(3,3)))    #[[1 2 3]                                        
#                                         # [4 5 6]
#                                         # [7 8 9]]
# code 2 ---------------------------------------------------------
change_array = numpy.array(list)
change_array.shape = (3, 3)

print(change_array)  

# ========== shape ==========
# The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array.
''' import numpy

arr = numpy.array([1, 2, 3, 4, 5])
print(arr.shape)     #(5,) -> 5 rows and 0 columns

arr = numpy.array([[1, 2],[3, 4],[6,5]])
print(arr.shape)     #(3, 2) -> 3 rows and 2 columns 

arr = numpy.array([1,2,3,4,5,6])
arr.shape = (3, 2)
print(arr)      

#Output
[[1 2]
 [3 4]
 [5 6]]  '''
# ========== reshape ==========
# The reshape tool gives a new shape to an array without changing its data. It creates a new array and does not modify the original array itself. 
''' import numpy
    
    my_array = numpy.array([1,2,3,4,5,6])
    print(numpy.reshape(my_array,(3,2)))
    
    #Output
    [[1 2]
     [3 4]
     [5 6]]  '''
