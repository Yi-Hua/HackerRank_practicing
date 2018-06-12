# Arrays
# numpy.array(input(),type) type = int, float, ...

# Input: A single line of input containing space separated numbers.
''' 1 2 3 4 -8 -10'''
# Output: Print the reverse NumPy array with type float.
''' [-10.  -8.   4.   3.   2.   1.] '''
import numpy

def arrays(arr):
    #code 1
    arr.reverse()
    return numpy.array(arr,float)
    
    #code 2
    ''' return(numpy.array(arr[::-1], float))    '''    #arr[a:b:c] : arr[a]~arr[b]中，隔著c個取
arr = input().strip().split(' ')
result = arrays(arr)

# code 3-------------------------------
# arr = input().strip().split(' ')
# arr.reverse()
# result = numpy.array(arr,float)    
#code 4-------------------------------
# arr = input().strip().split(' ')
# result = numpy.array(arr[::-1], float)
print(result)

