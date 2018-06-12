# Mod Divmod

# For example: 
''' >>> print divmod(177,10)
    (17, 7)'''
# Here, the integer division is 177/10 => 17 and the modulo operator is 177%10 => 7.

# Sample Input 
''' 177
    10  '''
# Sample Output 
''' 17
    7
    (17, 7) '''

a = int(input())
b = int(input())
print(a//b)
print(a%b)
print(divmod(a,b))