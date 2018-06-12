# Set .symmetric_difference() Operation 對稱差
#    ______
#   |      |
#   | A ...|___     A union B : A.symmetric_difference(B)  or  A^B
#   |___:..:   |
#       |    B |
#       |______|

# Sample Input
'''
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8   '''
# Sample Output
''' 8  '''

a = input()
A = set(input().split())
b = input()
B = set(input().split())
C = A.symmetric_difference(B)
# C = A^B
print(len(C))

# =========== .symmetric_difference() ==========
# The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
# Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
# The set is immutable to the .symmetric_difference() operation (or ^ operation).
'''
>>> s = set("Hacker")
>>> print s.symmetric_difference("Rank")
set(['c', 'e', 'H', 'n', 'R', 'r'])

>>> print s.symmetric_difference(set(['R', 'a', 'n', 'k']))
set(['c', 'e', 'H', 'n', 'R', 'r'])

>>> print s.symmetric_difference(['R', 'a', 'n', 'k'])
set(['c', 'e', 'H', 'n', 'R', 'r'])

>>> print s.symmetric_difference(enumerate(['R', 'a', 'n', 'k']))
set(['a', 'c', 'e', 'H', (0, 'R'), 'r', (2, 'n'), 'k', (1, 'a'), (3, 'k')])

>>> print s.symmetric_difference({"Rank":1})
set(['a', 'c', 'e', 'H', 'k', 'Rank', 'r'])

>>> s ^ set("Rank")
set(['c', 'e', 'H', 'n', 'R', 'r'])     '''