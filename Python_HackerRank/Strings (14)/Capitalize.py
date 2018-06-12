#Capitalize! 大寫

#You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
#For example, alison heck should be capitalised correctly as Alison Heck. 
''' alison heck => Alison Heck  '''
#Given a full name, your task is to capitalize the name appropriately.

# Input
''' chris alan 1w '''
# Output
''' Chris Alan 1w '''

def capitalize(string):  
    l = string.split(" ")               #['chris', 'alan', '1w']
    a = [i.capitalize() for i in l]     #['Chris', 'Alan', '1w']      
    return " ".join(a)




if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)