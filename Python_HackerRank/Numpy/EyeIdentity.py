# Eye and Identity: Your task is to print an array of size NxM with its main diagonal elements as 1's and 0's everywhere else.

# Input
''' 3 3 '''
# Output
''' [[ 1.  0.  0.]
    [ 0.  1.  0.]
    [ 0.  0.  1.]]  '''
# -------------------------------------------------------------------------
import numpy

# numpy.set_printoptions(sign=' ')
# print(numpy.eye(*map(int, input().split())))

a, b = map(int,input().split())   
I = numpy.eye(a, b)
print(I)
# --------------------------------------------------------------------------
# ======== Identity ========
'''
import numpy
print(numpy.identity(3))    ''' #3 is for  dimension 3 X 3

#Output
'''
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
 '''
# ========== Eye ==========
'''
import numpy
print(numpy.eye(8, 7, k = 1))   '''    # 8 X 7 Dimensional array with first upper diagonal 1.

#Output
'''
[[ 0.  1.  0.  0.  0.  0.  0.]
 [ 0.  0.  1.  0.  0.  0.  0.]
 [ 0.  0.  0.  1.  0.  0.  0.]
 [ 0.  0.  0.  0.  1.  0.  0.]
 [ 0.  0.  0.  0.  0.  1.  0.]
 [ 0.  0.  0.  0.  0.  0.  1.]
 [ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.]]     '''

'''
print(numpy.eye(8, 7, k = -2))  '''     # 8 X 7 Dimensional array with second lower diagonal 1.

#Output
'''
[[ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.]
 [ 1.  0.  0.  0.  0.  0.  0.]
 [ 0.  1.  0.  0.  0.  0.  0.]
 [ 0.  0.  1.  0.  0.  0.  0.]
 [ 0.  0.  0.  1.  0.  0.  0.]
 [ 0.  0.  0.  0.  1.  0.  0.]
 [ 0.  0.  0.  0.  0.  1.  0.]] '''