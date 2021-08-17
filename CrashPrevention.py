#Ethan Kupka
#Exception- Fixing a crash
#Oct 10, 2019

try:
    ques = int(input("Give a word "))

except ValueError:

    print("thank you")


try:
    infile = open("nothing", "r")

except IOError:
    print("Cool")

'''
a. Write a program that crashes when a user gives a file name for reading that doesn't exist.
b. Fix this crash using exceptions
c. Write a program that crashes when a user gives a word when the program wants a number.
d. Fix this crash using exceptions
'''
