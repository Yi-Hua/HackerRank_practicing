    arr = [] 
    for i in range(int(raw_input())):
        s = raw_input().split()
    for i in range(1,len(s)):
        s[i] = int(s[i])
        if s[i] == 0:
            insert(s[i], 5)
        else:
            arr[i] = s[i]