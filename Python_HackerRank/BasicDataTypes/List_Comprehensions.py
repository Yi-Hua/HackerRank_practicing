#List Comprehensions

# Input 0
''' 1
    1
    1
    2   '''
# Output 0
''' [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]] '''

# Input 1
''' 2
    2
    2
    2   '''
# Output 1
''' [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]] '''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list = [[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ]
    print(list)


# Python.
''' python 
    x = int ( input()) 
    y = int ( input()) 
    n = int ( input()) 
    ar = [] 
    p = 0 
    for i in range ( x + 1 ) : 
        for j in range( y + 1): 
            if i+j != n: ar.append([]) 
                ar[p] = [ i , j ] 
                p+=1 
                print(ar)     '''
# Other smaller codes may also exist, but using list comprehensions is always a good option. Code using list comprehensions:
''' python 
    x = int (input()) 
    y = int (input()) 
    n = int (input()) 
    print([ [ i, j] for i in range(x + 1) for j in range( y + 1) if ( ( i + j ) != n ) ])    '''