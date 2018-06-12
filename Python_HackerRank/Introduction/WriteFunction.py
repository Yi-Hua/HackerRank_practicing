# Write a function

''' We add a Leap Day on February 29, almost every four years. 
    The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February. 
    In the Gregorian calendar three criteria must be taken into account to identify leap years:
    # The year can be evenly divided by 4, is a leap year, unless: 
    # The year can be evenly divided by 100, it is NOT a leap year, unless: 
    # The year is also evenly divisible by 400. Then it is a leap year.   '''

# Task: You are given the year, and you have to write a function to check if the year is leap or not. 
# Note that you have to complete the function and remaining code is given as template. 

def is_leap(year):
    leap = False
    if 1900<= year <= 10**5:
        if year % 400 == 0:
            return not leap
        elif year % 100 == 0:
            return leap
        elif year % 4 == 0:
            return not leap
        else:
            return leap
    
    return leap

year = int(input())
print(is_leap(year))