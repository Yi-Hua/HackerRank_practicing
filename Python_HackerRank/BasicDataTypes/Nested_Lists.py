# Nested Lists
''' Given the names and grades for each student in a Physics class of N students,
    store them in a nested list and print the name(s) of any student(s) having the second lowest grade. '''
#Input Format
''' The first line contains an integer, N , the number of students. 
The 2N subsequent lines describe each student over 2 lines; 
the first line contains a student's name, and the second line contains their grade. '''
# Output Format
''' Print the name(s) of any student(s) having the second lowest grade in Physics; 
    if there are multiple students, order their names alphabetically and print each one on a new line. '''
# Input 0
''' 5
    Harry
    37.21
    Berry
    37.21
    Tina
    37.2
    Akriti
    41
    Harsh
    39  '''
# Output 0
''' Berry
    Harry   '''

if __name__ == '__main__':
    n = int(input())
    studentscore = []
    scorelist = []

    for i in range(n):
        name = input()
        score = float(input())
        studentscore.append([name, score])
        scorelist.append(score)
    a = sorted(set(scorelist))[1] # second lowest grade
    secondlowest_Name = []
    for i in range(n):
        if scorelist[i] == a:
           secondlowest_Name.append(studentscore[i][0])
    secondlowest_Name = sorted(secondlowest_Name) #sorted(): 字母按順序
    for i in range(len(secondlowest_Name)):
          print(secondlowest_Name[i])

