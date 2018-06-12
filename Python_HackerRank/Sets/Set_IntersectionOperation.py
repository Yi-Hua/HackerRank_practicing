# Set .intersection() Operation 交集
#   ........
#   :      :
#   : A  __:....     A intersection B : A.intersection(B)  or  A&B
#   :...|__|   :
#       :    B :
#       :......:

# Sample Input
'''
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8   '''
# Sample Output
''' 5  '''

a = input()
A = set(input().split())
b = input()
B = set(input().split())
C = A.intersection(B)
# C = A&B
print(len(C))


# ========== .intersection() ==========
# The .intersection() operator returns the intersection of a set and the set of elements in an iterable.
# Sometimes, the & operator is used in place of the .intersection() operator, but it only operates on the set of elements in set.
# The set is immutable to the .intersection() operation (or & operation).
''' 
>>> s = set("Hacker")
>>> print s.intersection("Rank")
set(['a', 'k'])

>>> print s.intersection(set(['R', 'a', 'n', 'k']))
set(['a', 'k'])

>>> print s.intersection(['R', 'a', 'n', 'k'])
set(['a', 'k'])

>>> print s.intersection(enumerate(['R', 'a', 'n', 'k']))
set([])

>>> print s.intersection({"Rank":1})
set([])

>>> s & set("Rank")
set(['a', 'k'])     '''