#Class 2 - Find the Torsional Angle 
'''
You are given four points A, B, C and D in a 3-dimensional Cartesian coordinate system. 
You are required to print the angle between the plane made by the points A, B, C and B, C, D in degrees(not radians). 
Let the angle be PHI.
Cos(PHI) = (X.Y)/|X||Y| where X = AB x BC and Y = BC x CD. 
Here, X.Y means the dot product of X and Y, and AB x BC means the cross product of vectors AB and BC. 
Also, AB = B - A.
'''
# Input : four points
''' 0 4 5
    1 7 6
    0 5 9
    1 7 2   '''
# Output    
''' 8.19    '''

import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    def __sub__(self, other):
        a = other.x-self.x
        b = other.y-self.y
        c = other.z-self.z
        return Points(a,b,c)
    def dot(self, other):
        d = self.x*other.x + self.y*other.y + self.z*other.z
        return d
    def cross(self, other):
        a = self.y*other.z-self.z*other.y
        b = self.z*other.x-self.x*other.z
        c = self.x*other.y-self.y*other.x
        return Points(a,b,c)
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)    #X = AB x BC
    y = (c - b).cross(d - c)    #Y = BC x CD
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))