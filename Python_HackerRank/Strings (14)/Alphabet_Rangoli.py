#Alphabet Rangoli
''' You are given an integer, N. 
    Your task is to print an alphabet rangoli of size N.
    (Rangoli is a form of Indian folk art based on creation of patterns.) '''
#size 3
''' ----c----
    --c-b-c--
    c-b-a-b-c
    --c-b-c--
    ----c----   '''
# Input
''' 5   '''
# Output
''' --------e--------
    ------e-d-e------
    ----e-d-c-d-e----
    --e-d-c-b-c-d-e--
    e-d-c-b-a-b-c-d-e
    --e-d-c-b-c-d-e--
    ----e-d-c-d-e----
    ------e-d-e------
    --------e--------   '''

import string
alpha = string.ascii_lowercase  #abcdefghijklmnopqrstuvwxyz

def print_rangoli(size):        # size = 5
    alpha1 = alpha[:size]       # abcde
    for i in range(1,size*2):
        if i <= size:
            k = i
        else:
            k = size*2-i
        line1 = alpha1[size-k:]      
        line2 = line1[1:]
        line = line2[::-1] + line1
        s = '-'.join(line).center(4*size-3)
        print(s.replace(' ','-'))



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)



#.ljust(width)
#This method returns a left aligned string of length width.
''' >>> width = 20
    >>> print 'HackerRank'.ljust(width,'-')
    HackerRank----------  
'''
#.center(width)
#This method returns a centered string of length width.
''' >>> width = 20
    >>> print 'HackerRank'.center(width,'-')
    -----HackerRank-----
'''
#.rjust(width)
#This method returns a right aligned string of length width.
''' >>> width = 20
    >>> print 'HackerRank'.rjust(width,'-')
    ----------HackerRank
'''