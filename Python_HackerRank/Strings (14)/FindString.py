#Find a string

# input:
''' ABCDCDC
    CDC     '''
# output:
''' 2 '''
  
def count_substring(string, sub_string):
    k = 0
    s = len(sub_string)
    for i in range(0,len(string)):        
        if string[i:i+s] == sub_string[0:s]:
            k = k + 1
    print(k)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

      

