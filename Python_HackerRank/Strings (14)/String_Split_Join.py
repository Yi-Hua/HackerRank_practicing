# String Split and Join : In Python, a string can be split on a delimiter. 
# join() 方法用於將序列中的元素以指定的字符連接生成一個新的字符串。
# Input 
''' this is a string  ''' 
# Output 
''' this-is-a-string  '''

def split_and_join(line):
    line = line.split(" ") #['this', 'is', 'a', 'string']
    str = '-'
    return str.join(line) 
    #line.replace(" ","-")


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)