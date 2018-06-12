#Classes: Dealing with Complex Numbers

# Input: 
''' 2 1  #C = 2 + 1i
    5 6  #D = 5 + 6i   '''
# Output
''' 7.00+7.00i      #C+D
    -3.00-5.00i     #C-D
    4.00+17.00i     #C*D
    0.26-0.11i      #C/D
    2.24+0.00i      #mod(C)
    7.81+0.00i      #mod(D)  '''

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary        
    def __add__(self, other):       #addition
        add_real = self.real + other.real
        add_imag= self.imaginary + other.imaginary
        return Complex(add_real, add_imag)

    def __sub__(self, other):       #Subtraction
        sub_real = self.real - other.real
        sub_imag= self.imaginary - other.imaginary
        return Complex(sub_real, sub_imag)

    def __mul__(self, other):       #multiplication
        mul_real = self.real*other.real-self.imaginary*other.imaginary
        mul_imag = self.real*other.imaginary + other.real*self.imaginary
        return Complex(mul_real, mul_imag)

    def __truediv__(self, other):   #division
        Deno = math.pow(other.real,2) + math.pow(other.imaginary,2)      #Denominator

        other.imaginary = -other.imaginary
        mole_real = self.real*other.real-self.imaginary*other.imaginary
        mole_imag = self.real*other.imaginary + other.real*self.imaginary
        Mole = complex(mole_real, mole_imag)     #Molecular
        
        m = Mole/Deno
        return Complex(m.real, m.imag)

    def mod(self):
        m = math.pow(self.real,2) + math.pow(self.imaginary,2)
        m = math.pow(m,0.5)
        return Complex(m.real, m.imag)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    # print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')