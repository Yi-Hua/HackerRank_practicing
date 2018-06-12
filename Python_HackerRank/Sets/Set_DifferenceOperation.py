# Set .difference() Operation 差集
#    ______
#   |      |
#   | A  __|....     A difference B : A.difference(B)  or  A-B
#   |___|      :
#       :    B :
#       :......:

# Sample Input
'''
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8   '''
# Sample Output
''' 4  '''

a = input()
A = set(input().split())
b = input()
B = set(input().split())
C = A.difference(B)
# C = A-B
print(len(C))




# ========== .difference() ========== 
# The tool .difference() returns a set with all the elements from the set that are not in an iterable.
# Sometimes the - operator is used in place of the .difference() tool, but it only operates on the set of elements in set.
# Set is immutable to the .difference() operation (or the - operation).
''' 
>>> s = set("Hacker")
>>> print s.difference("Rank")
set(['c', 'r', 'e', 'H'])

>>> print s.difference(set(['R', 'a', 'n', 'k']))
set(['c', 'r', 'e', 'H'])

>>> print s.difference(['R', 'a', 'n', 'k'])
set(['c', 'r', 'e', 'H'])

>>> print s.difference(enumerate(['R', 'a', 'n', 'k']))
set(['a', 'c', 'r', 'e', 'H', 'k'])

>>> print s.difference({"Rank":1})
set(['a', 'c', 'e', 'H', 'k', 'r'])

>>> s - set("Rank")
set(['H', 'c', 'r', 'e'])   '''