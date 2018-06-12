# Polar Coordinates

# Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.
# A complex number z = x + yj is completely determined by its real part x and imaginary part y . 
# Here, j is the imaginary unit.
# A polar coordinate (r,p) is completely determined by modulus r(長) and phase angle p(弧度).

# ========== cmath.phase ========== 
''' >>> phase(complex(-1.0, 0.0))
    3.1415926535897931              '''
# ========== abs ========== 
''' >>> abs(complex(-1.0, 0.0))
    1.0                             '''

# Sample Input
''' 1+2j    '''
# Sample Output
''' 2.23606797749979 
    1.1071487177940904  '''


a = complex(input())
print (abs(a))
import cmath 
print(cmath.phase(a)) #弧度