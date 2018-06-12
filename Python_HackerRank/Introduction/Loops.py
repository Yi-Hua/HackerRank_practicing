# Loops

# Task : Read an integer N. For all non-negative integers i<N, print i**2.

# Sample Input 0
''' 5   '''
# Sample Output 0
''' 0       
    1
    4
    9
    16  '''

if __name__ == '__main__':
    n = int(input())
    for a in range(0,n):
        print(a**2, sep='\n')