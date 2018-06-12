#Introduction to Sets : A set is an unordered collection of elements without duplicate entries. 
#                       When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.
'''[2,3,2,2,1,3,4] => [1,2,3,4]'''
'''Hanker => [a, e, h, k, n, r]'''
#Input
''' 10
161 182 161 154 176 170 167 171 170 174 '''
#Output
''' 169.375 '''
def average(array):
    # your code goes here
    set_arr = set(array)
    average_set = sum(set_arr)/len(set_arr)
    return average_set 

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)    


'''
>>> print(set())
set([])

>>> print(set('HackerRank'))
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

>>> print(set([1,2,1,2,3,4,5,6,0,9,12,22,3]))
set([0, 1, 2, 3, 4, 5, 6, 9, 12, 22])

>>> print(set((1,2,3,4,5,5)))
set([1, 2, 3, 4, 5])

>>> print(set(set(['H','a','c','k','e','r','r','a','n','k'])))
set(['a', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print(set({'Hacker' : 'DOSHI', 'Rank' : 616 }))
set(['Hacker', 'Rank'])

>>> print(set(enumerate(['H','a','c','k','e','r','r','a','n','k'])))
set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])
'''