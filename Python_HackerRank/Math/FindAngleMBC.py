# Find Angle MBC

# Problem:
# Triangle ABC is a right triangle, 90° degrees at B.
# Point M is the midpoint of hypotenuse AC.
# You are given the lengths AB and BC. 
# Your task is to find angle MBC in degrees.

# Note: Round the angle to the nearest integer.
# Examples: 
# If angle is 56.5000001°, then output 57°. 
# If angle is 56.5000000°, then output 57°. 
# If angle is 56.4999999°, then output 56°. 

# Sample Input
''' 10
    10  '''
# Sample Output
''' 45° '''

import cmath
from math import degrees
 
A = complex(0.0 , float(input()))
B = complex(float(input()), 0.0)
M = (A+B)/2
angle = round(degrees(cmath.phase(M)))
print(str(angle)+'°')







