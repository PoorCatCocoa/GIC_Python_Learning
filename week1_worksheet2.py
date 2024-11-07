import math

# Q1
width = int(input("Please enter the width of the rectangle: "))
height = int(input("Please enter the height of the rectangle: "))
rectangle = width *height
print(rectangle)

#Q2
types_choose = int(input("\nPress 1 for Sum\nPress 2 for Difference\nPress 3 for Product\nPress 4 for Quotient\nPlease choose the type to calculate: "))
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
match types_choose:
    case 1: print (num1 + num2)
    case 2: print (num1 - num2)
    case 3: print (num1 * num2)
    case 4: print (num1 / num2)

#Q3
print(type(input("Enter to check the type of input")))

#Q4
"""
#a
(a*b*(c-d))^2 + (e/3 + f/4)
square brackets a times b times brackets c minus d plus brackets e divide 3 plus f divide 4
#b
(a*b*(c-d))^2 + e/3 + f/4
"""

#Q5
"""
#a
7
#b
17, 18
#c
2
#d
5, 6
#e
str
"""

#6
"""
#a
We need 1 more piece(s) of paper
#b
A program use to check if users name are Alice or Bob
"""