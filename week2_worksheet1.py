#Q1
#a
movie_list = ['1', '2', '3']
movie_list += "4"
print(movie_list[1])
del(movie_list[2])
movie_list.insert(1, "5")
print(movie_list)
#b
fruit = ['apples', 'bananas', 'pears', 'peaches']
print(fruit[-1])
print(fruit[0])
print(fruit[0:2])
fruit.append("grapes")
print(fruit.index("grapes"))
print(fruit[1])

#Q2
#a
"""
1. when we making timetable
2. when we making plans
3. when we making 
"""
#b
person = ('Bob', '30', 'Engineer')
print(person[:2])
person = ('Bob', '30', 'Computer scientist')
(a, b, c) = person

#Q3
#a
Animals = {'Cat', 'Dog', 'Bird'}
Animals.add("Fish")
Animals.add("Dog")
print(Animals)
#b
"""
Set is unordered, and not allowed duplicate elements
"""

#Q4
#a
"""
We should use dict() to making a dictionary for the words
"""
#b
Grades = {'Alice': 79, 'Bob': 35, 'Charlie': 64, 'David': 75, 'Eve': 81}
print(Grades["Alice"])
del(Grades["Bob"])

#Q5
#a
"""
I will use dict()
"""
#b
student_module_scores = {"A": 80, "B": 85, "C": 70, "D": 95}
y = {"A": 75, "B": 95, "C": 70, "D": 95}
student_module_scores.update(y)