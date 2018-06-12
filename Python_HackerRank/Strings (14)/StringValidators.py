#String Validators
#input:
''' qA2 '''
#output:
''' True
    True
    True
    True
    True
'''
if __name__ == '__main__':
    S = input()
    print(any(c.isalnum() for c in S))
    print(any(c.isalpha() for c in S))
    print(any(c.isdigit() for c in S))
    print(any(c.islower() for c in S))
    print(any(c.isupper() for c in S))
'''
any() : 用於判斷給定的可迭代參數 iterable 是否全部為空對象，
        如果都為空、0、false，則返回 False，
        如果不都為空、0、false，則返回 True。
'''
# ========== str.isalnum() ========== 
#This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
'''
>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False
'''
# ========== str.isalpha() ==========  
#This method checks if all the characters of a string are alphabetical (a-z and A-Z).
'''
>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False
'''
# ========== str.isdigit() ==========  
#This method checks if all the characters of a string are digits (0-9).
''''
>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False
'''
# ========== str.islower() ==========  
#This method checks if all the characters of a string are lowercase characters (a-z).
'''
>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False
'''
# ========== str.isupper() ==========  
#This method checks if all the characters of a string are uppercase characters (A-Z).
'''
>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False
'''