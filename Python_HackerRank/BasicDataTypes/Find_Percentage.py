# Finding the percentage
''' You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. 
    The marks can be floating values. 
    The user enters some integer N followed by the names and marks for N students. 
    You are required to save the record in a dictionary data type. 
    The user then enters a student's name. 
    Output the average percentage marks obtained by that student, correct to two decimal places.    '''
# Input 
''' 2
    Harsh 25 26.5 28
    Anurag 26 28 30
    Harsh   '''
# Output 
''' 26.50   ''' #(25+26.5+28)/3=26.5

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    list = student_marks[query_name]
    sum = 0
    for item in list:
        sum += item
    print("{:.2f}".format(sum/len(list),2))

    
''' {:.2f}.format() : 3.1415926  ->  3.14   保留小數點後兩位
    {:+.2f}.format(): 3.1415926  ->  +3.14  帶符號保留小數點後兩位
    {:+.2f}.format():        -1  ->  -1.00  帶符號保留小數點後兩位
    {:.0f}.format():    2.71828  ->  3      不帶小數
    {:0>2d}.format():         5  -> 05      數字補零 (填充左邊, 寬度為2) 
    {:x<4d}.format():         5  -> 5xxx    數字補x (填充右邊, 寬度為4)
    {:x<4d}.format():        10  -> 10xx    數字補x (填充右邊, 寬度為4)
    {:,}.format():      1000000  -> 1,000,000以逗號分隔的數字格式
    {:.2%}.format():       0.25  -> 25.00%   百分比格式
    {:.2e}.format():10000000001  -> .00e+09  指數記法
    {:10d}.format():    13 ->         13     右對齊 (默認, 寬度為10)
    {:<10d}.format():   13 -> 13             左對齊 (寬度為10)
    {:^10d}.format():   13 ->     13         中間對齊 (寬度為10)
    11
        '{:b}'.format(11) -> 1011       進制
        '{:d}'.format(11) -> 11
        '{:o}'.format(11) -> 13
        '{:x}'.format(11) -> b
        '{:#x}'.format(11) -> 0xb
        '{:#X}'.format(11) -> 0XB           '''





