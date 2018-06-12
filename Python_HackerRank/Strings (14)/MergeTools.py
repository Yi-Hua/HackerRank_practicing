# Merge the Tools! 合併Tools
''' Consider the following:
1. A string,s, of length n where s = c_0c_1...c_(n-1).
2. An integer, k, where k is a factor of n '''
# We can split n into n/k subsegments where each subsegment, ti, consists of a contiguous block of k characters in s. 
# Then, use each ti to create string ui such that:
''' 1. The characters in ui are a subsequence of the characters in ti.
    2. Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. 
       In other words, if the character at some index j in ti occurs at a previous index <j in ti, then do not include the character in string ui.  '''
# Given s and k, print n/k lines where each line i denotes string ui. 
# Input
''' AABCAAADA
    3   '''   
# Output
''' AB
    CA
    AD  '''
def merge_the_tools(string, k):         # string = 'AABCAAADA'  ; k=3
    n = len(string)                     # n = 9
    for i in range(0,n,k): 
        X = string[i:i+k]               #(i,X) = (0,AAB) (3,CAA) (6,ADA)'''
    #===Method 1=== 
        # X_ = list(set(X))             # X_ = ['A','B'] ['C', 'A'] ['D', 'A']...[set()為無序不重複集合]
        # X_.sort(key = X.index)        # sort():排序，排與X同順序
    #===Method 2===
        X_ = sorted(set(X),key = X.index)       #sort 是應用在 list 上的方法，sorted 可以對所有可迭代的對象進行排序操作。
                                                #list 的 sort 方法返回的是對已經存在的列表進行操作，
                                                #而內建函數 sorted 方法返回的是一個新的 list，而不是在原來的基礎上進行的操作。
    #===Method 3===
        # X_ = []
        # for i in X:
        #     if not i in X_:
        #         X_.append(i)
    #===Method 4===
        # X_ = []
        # [X_.append(i) for i in X if not i in X_]
    #==============    
        print(''.join(X_))          # join():將序列中的元素以指定的字符，連接生成一個新的字符串


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)




'''
如果要保持他们原來的排序：
-----------sort()------------  
一、用list的sort方法
l1 = ['b','c','d','b','c','a','a']
l2 = list(set(l1))
l2.sort(key = l1.index)
print(l2)

二、也可以這樣寫
l1 = ['b','c','d','b','c','a','a']
l2 = sorted(set(l1),key = l1.index)
print l2
 
----------append()----------
三、也可以用遍歷
l1 = ['b','c','d','b','c','a','a']
l2 = []
for i in l1:
    if not i in l2:
        l2.append(i)
print l2

四、上面的代碼也可以這樣寫
l1 = ['b','c','d','b','c','a','a']
l2 = []
[l2.append(i) for i in l1 if not i in l2]
print l2
'''