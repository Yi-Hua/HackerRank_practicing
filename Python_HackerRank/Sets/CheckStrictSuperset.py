# Check Strict Superset (Strict : A is not equival to B) 超集合
#    _________
#   | B  ____ |     A is a subset of a set B
#   |   |  A ||     B is a superset of A    
#   |   |____||
#   |_________|

# Example 
# Set([1, 3, 7]) is a strict superset of set([1,3]). 
# Set([1, 3, 7]) is not a strict superset of set([1, 3, 7]). 
# Set([1, 3, 7]) is not a strict superset of set([1, 3, 5]). 

# Sample Input 0
'''
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12   '''
# Sample Output 0
''' False   '''


A = set(input().split())
n = int(input())
t = 0
for _ in range(n):
    B = set(input().split())
    if bool(len(A-B) == len(A) - len(B)) == False:
        t = 1
print(bool(t == 0))
    
