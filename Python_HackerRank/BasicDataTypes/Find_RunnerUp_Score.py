#Find the Runner-Up Score!
''' Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
    You are given n scores. Store them in a list and find the score of the runner-up.   '''
# Input 0
''' 5
    2 3 6 6 5   '''
# Output 0
''' 5   '''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # code 1
    ''' print( sorted(set(arr))[-2] ) ''' # set(): 重複的被删除
                                        # x & y :交集
                                        # x | y :聯集
                                        # x - y :差集
    # code 2
    list = list(arr)
    l = [x for x in list if x != max(list)]
    print(max(l))
    
