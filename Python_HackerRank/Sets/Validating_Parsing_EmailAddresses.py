# Validating and Parsing Email Addresses

# A valid email address meets the following criteria: 
# It's composed of a username, domain name, and extension assembled in this format: username@domain.extension 
# The username starts with an English alphabetical character, 
# and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _. 
# The domain and extension contain only English alphabetical characters. 
# The extension is 1, 2 or 3 characters in length.

# Sample Input
'''
2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>
'''
# Sample Output
''' DEXTER <dexter@hotmail.com>     '''

import email.utils
n = int(input())
for _ in range(n):
    T = input().split()
    t = 1               # true
    intex = 0
    for i, j in enumerate(T[1][1:-1]):
        if j == '@':
            intex = i
        if j == '.':
            if intex == 0:
                t = 0 
            else:
                
            
    ans = 1
    if t == 1:
        ans = 0
    elif T[1][intex:].islower() != True:
        ans = 0            
    elif T[1][0].islower() != True:
        ans = 0  

    if ans == 1:
        A = [T[0],T[1][1:-1]]
        print(email.utils.formataddr(A))
    else:
        print('')

# Hint: Try using Email.utils() to complete this challenge. For example, this code: 
'''
import email.utils
print email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')
print email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))
'''
# produces this output:
'''
('DOSHI', 'DOSHI@hackerrank.com')
DOSHI <DOSHI@hackerrank.com>
'''    
    