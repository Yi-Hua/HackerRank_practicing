#Text Wrap

# Input 0
''' ABCDEFGHIJKLIMNOQRSTUVWXYZ
    4                          '''
# Output 0
''' ABCD
    EFGH
    IJKL
    IMNO
    QRST
    UVWX
    YZ    '''

def wrap(string, max_width):
    string = string.strip()
    X = []
    for i in range(0,len(string)-1,max_width):
        X.append(string[i:max_width+i])
        print(i, X)
        #print(i, max_width+i)
        #print(string[i:max_width+i])
    return '\n'.join(X)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)