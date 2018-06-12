# Floor, Ceil and Rint 
# Sample Input
''' 1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9 '''
# Sample Output
''' [ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
    [  2.   3.   4.   5.   6.   7.   8.   9.  10.]
    [  1.   2.   3.   4.   6.   7.   8.   9.  10.]  '''

import numpy

numpy.set_printoptions(sign=' ')    #np.set_printoptions( 列印選項 ): 設定列印格式。
# 參考: https://www.brilliantcode.net/1045/numpy-tutorial-how-to-print-array/

my_array = numpy.array(input().split(),float)
print(numpy.floor(my_array))
print(numpy.ceil(my_array))
print(numpy.rint(my_array))




# ========== floor() ==========
# The tool floor returns the floor of the input element-wise. 
# The floor of x is the largest integer i where i <= x.
'''
import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(numpy.floor(my_array))         # output: [ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
'''
# ========== ceil() ==========
# The tool ceil returns the ceiling of the input element-wise. 
# The ceiling of x is the smallest integer i where i >= x.
'''    
import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(numpy.ceil(my_array))           # output: [  2.   3.   4.   5.   6.   7.   8.   9.  10.]
'''
# ========== rint() ==========  
# The rint tool rounds to the nearest integer of input element-wise. 最接近的整數 (即四捨五入)
''' 
import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(numpy.rint(my_array))           # output: [  1.   2.   3.   4.   6.   7.   8.   9.  10.]
'''
