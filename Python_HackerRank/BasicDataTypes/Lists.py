# Lists
''' Consider a list (list = []). You can perform the following commands: 
    1. insert i e: Insert integer e at position i.
    2. print: Print the list.
    3. remove e: Delete the first occurrence of integer e.
    4. append e: Insert integer e at the end of the list. 
    5. sort: Sort the list.
    6. pop: Pop the last element from the list.
    7. reverse: Reverse the list.  '''
# Input 0
''' 12
    insert 0 5
    insert 1 10
    insert 0 6
    print
    remove 6
    append 9
    append 1
    sort
    print
    pop
    reverse
    print   '''
# Output 0
''' [6, 5, 10]
    [1, 5, 9, 10]
    [9, 5, 1]   '''

if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(1,N+1):
        s = input().split()  
        if s[0] == 'insert' :
            a, b = int(s[1]), int(s[2])
            arr.insert(a, b)                # insert(a, b):第a的位置放b   
        elif s[0] == 'print' :
            print(arr)
        elif s[0] == 'remove':
            a = int(s[1])
            arr.remove(a)                   # remove(a):移除"一個"a
        elif s[0] == 'append':
            a = int(s[1])
            arr.append(a)                   # append(a):增加a
        elif s[0] == 'sort':
            arr.sort()                      # sort():排序
        elif s[0] == 'pop':
            arr.pop()                       # pop():移除最後一項
        elif s[0] == 'reverse':
            arr.reverse()                   # reverse():倒敘
            
        
        
