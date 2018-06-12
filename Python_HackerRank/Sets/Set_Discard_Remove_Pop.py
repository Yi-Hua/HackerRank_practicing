# Set .discard(), .remove() & .pop()

# Task :
# You have a non-empty set s, and you have to execute N commands given in N lines.
# The commands will be pop, remove and discard. 

# Sample Input
''' 9                   # 9 numbers
    1 2 3 4 5 6 7 8 9
    10                  # 10 lines    
    pop
    remove 9
    discard 9
    discard 8
    remove 7
    pop 
    discard 6
    remove 5
    pop 
    discard 5       '''
# Sample Output
''' 4   '''

n = int(input())
s = set(map(int, input().split()))

l = int(input())
for i in range(l):
    k = input().split()        #type(k) : list ,  type(k[i]) : str
    if k[0] == 'pop':
        s.pop()
    elif k[0] == 'remove':
        s.remove(int(k[1]))
    elif k[0] == 'discard':
        s.discard(int(k[1]))
print(sum(s))







# ========== .remove(x) ========== 
# This operation removes element x from the set. 
# If element x does not exist, it raises a KeyError.
# The .remove(x) operation returns None.
''' Example
>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.remove(5)
>>> print(s)
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print(s.remove(4))          
None                            # The .remove(x) operation returns None.
>>> print(s)
set([1, 2, 3, 6, 7, 8, 9])
>>> s.remove(0)                 
KeyError: 0     '''             # If element x does not exist, it raises a KeyError.

# ========== .discard(x) ========== 
# This operation also removes element x from the set. 
# If element x does not exist, it "does not" raise a KeyError.
# The .discard(x) operation returns None.
''' Example
>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.discard(5)
>>> print(s)
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print(s.discard(4))
None                                    # The .discard(x) operation returns None.
>>> print(s)
set([1, 2, 3, 6, 7, 8, 9])
>>> s.discard(0)
>>> print(s)
set([1, 2, 3, 6, 7, 8, 9])  '''         # If element x does not exist, it "does not" raise a KeyError.

# ========== .pop() ========== 
# This operation removes and return an arbitrary element from the set. 
# If there are no elements to remove, it raises a KeyError.
''' Example
>>> s = set([1])
>>> print(s.pop())
1
>>> print(s)
set([])
>>> print(s.pop())
KeyError: pop from an empty set     '''