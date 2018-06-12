# Set Mutations


# Sample Input
''' 
 16                                         # the number of elements in set A.            
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52     # the space separated list of elements in set A.
 4                                          # the number of other sets.
 intersection_update 10                    
 2 3 5 6 8 9 1 4 7 11                       # other set 1
 update 2
 55 66                                      # other set 2
 symmetric_difference_update 5
 22 7 35 62 58                              # other set 3            
 difference_update 7
 11 22 35 55 58 62 66                       # other set 4           ''' 
# Sample Output
''' 38      '''

A_num = int(input())
A = set(input().split())
Other_sets = int(input())
for i in range(Other_sets):
    operation_string = input().split()
    B = set(input().split())
    if operation_string[0] == 'intersection_update':
        A.intersection_update(B)
    elif operation_string[0] == 'update':
        A.update(B)
    elif operation_string[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(B)
    elif operation_string[0] == 'difference_update':
        A.difference_update(B)
print(sum(map(int, A)))  # map(fun,):映射



# ========== .update() or |=  ========== 
# Update the set by adding elements from an iterable/another set.
'''
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H 
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])       '''
# ========== .intersection_update() or &=  ========== 
# Update the set by keeping only the elements found in it and an iterable/another set.
'''
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.intersection_update(R)
>>> print H
set(['a', 'k'])     '''
# ========== .difference_update() or -=  ========== 
# Update the set by removing elements found in an iterable/another set.
'''
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.difference_update(R)
>>> print H
set(['c', 'e', 'H', 'r'])       '''
# ========== .symmetric_difference_update() or ^=  ========== 
# Update the set by only keeping the elements found in either set, but not in both.
'''
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.symmetric_difference_update(R)
>>> print H
set(['c', 'e', 'H', 'n', 'r', 'R']) '''