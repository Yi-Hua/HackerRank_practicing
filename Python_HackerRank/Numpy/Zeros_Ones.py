#Zeros and Ones

# Input 0
''' 3 3 3   '''
# Output 0
''' [[[0 0 0]
      [0 0 0]
      [0 0 0]]

     [[0 0 0]
      [0 0 0]
      [0 0 0]]

     [[0 0 0]
      [0 0 0]
      [0 0 0]]]
    [[[1 1 1]
      [1 1 1]
      [1 1 1]]

     [[1 1 1]
      [1 1 1]
      [1 1 1]]

     [[1 1 1]
      [1 1 1]
      [1 1 1]]]         '''

import numpy as np

input_number = tuple(map(int, input().strip().split()))   #tuple :  不可變動（Immutable）物件   ex:  (3,3,3)
print(np.zeros(input_number, dtype = np.int))       #list :   可變動（Mutable）物件       ex:  [3,3,3]
print(np.ones(input_number, dtype = np.int))

#-----------------------------------------------------------------------------------------------------------
# =====
# Zeros
# ===== 
# The zeros tool returns a new array with a given shape and type filled with 0's.
'''
import numpy
print(numpy.zeros((1,2)))   '''              # Default type is float
#Output: 
''' [[ 0.  0.]] '''

'''
print(numpy.zeros((1,2), dtype = numpy.int))  ''' #Type changes to int 
#Output: 
''' [[0 0]] '''
# ====                       
# Ones
# ==== 
# The ones tool returns a new array with a given shape and type filled with 1's.
''' import numpy
print(numpy.ones((1,2))) '''                    #Default type is float
#Output : 
''' [[ 1.  1.]]   '''

'''
print(numpy.ones((1,2), dtype = numpy.int)) ''' #Type changes to int
#Output : 
''' [[1 1]] '''
