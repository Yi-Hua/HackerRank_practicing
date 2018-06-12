# Set .union() Operation  聯集
#    ______
#   |      |
#   | A  __|___     A union B : A.union(B)  or  A|B
#   |___|__|   |
#       |    B |
#       |______|

# Sample Input
'''
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8   '''
# Sample Output
''' 13  '''

a = input()
A = set(input().split())
b = input()
B = set(input().split())
C = A.union(B)
# C = A|B
print(len(C))






# =========== .union() ===========
# The .union() operator returns the union of a set and the set of elements in an iterable. 
# Sometimes, the | operator is used in place of .union() operator, but it operates only on the set of elements in set.
# Set is immutable to the .union() operation (or | operation).

# Example
'''
>>> s = set("Hacker")
>>> print(s.union("Rank"))
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print(s.union(set(['R', 'a', 'n', 'k'])))
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print(s.union(['R', 'a', 'n', 'k']))
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print(s.union(enumerate(['R', 'a', 'n', 'k'])))
set(['a', 'c', 'r', 'e', (1, 'a'), (2, 'n'), 'H', 'k', (3, 'k'), (0, 'R')])

>>> print(s.union({"Rank":1}))
set(['a', 'c', 'r', 'e', 'H', 'k', 'Rank'])

>>> s | set("Rank")
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])   '''