#Q1
#list
#int
#9
#8, 15
"""
Line1: name a list temperature
Line5: define a function which check if the temp in temperatures higher than threshold
line12: define a function which do basic same as last one but save the temp higher into a list indices
"""

#Q2
def matrix_count(column, row):
    matrix = [[column for column in range(column)] for row in range(row)]
    cunt, i = 0, 0
    for length in matrix:
        cunt += matrix[i][i]
        i += 1
    return matrix

#Q3
def common_elements(list1, list2):
    fin = []
    for i in list2:
        for j in list1:
            if list1[j-1] == list2[i-1]:
                fin.append(list1[j-1])
    return fin

#Q4
def is_palindrome(word):
    if word[0] == word[-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

#Q5
