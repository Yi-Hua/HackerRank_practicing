# Print Function

# Read an integer N. 
# Without using any string methods, try to print the following: 123...N

# Sample Input 0
''' 3   '''
# Sample Output 0
''' 123 '''

if __name__ == '__main__':
    n = int(input())
    print(*range(1,n+1),sep='')