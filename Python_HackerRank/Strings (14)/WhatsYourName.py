#What's Your Name?:

''' Hello [firstname] [lastname]! You just delved into python.'''

#Input 
''' Ross
    Taylor'''
#Output 
''' Hello Ross Taylor! You just delved into python.'''

def print_full_name(a, b):
    print("Hello "+str(a)+" "+str(b)+"! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)