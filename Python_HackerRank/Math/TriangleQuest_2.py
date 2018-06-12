# Triangle Quest 2

# For example, a palindromic triangle of size 5 is: 
''' 1
    121
    12321
    1234321
    123454321   '''
# You can't take more than two lines. The first line (a for-statement) is already written for you. 
# You have to complete the code using exactly one print statement. 

# Note: 
# Using anything related to strings will give a score of 0. 
# Using more than one for-statement will give a score of 0.

# Sample Input
''' 5   '''
# Sample Output
''' 1
    121
    12321
    1234321
    123454321   '''


for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**i//9)**2)