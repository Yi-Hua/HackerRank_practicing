# Tuples
# Task : 
''' Given an integer, n , and n space-separated integers as input, create a tuple, t , of those n integers. 
    Then compute and print the result of  hash().
    Note: hash() is one of the functions in the __builtins__ module, so it need not be imported. '''
#Input
''' 2
    1 2 '''
#Output
''' 3713081631934410656 '''

if __name__ == '__main__':
    n = int(input())
    '''integer_list = input().split()'''                # ['1', '2', '3', '4'] 

    integer_list = map(int, input().split())            # [1, 2, 3, 4]
    '''integer_list = [int(x) for x in input_list]'''   
    t = tuple(integer_list)                             # (1, 2, 3, 4)
    print(hash(t))