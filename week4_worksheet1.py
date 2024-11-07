def func1(a, b):
    return a+b
result = func1(1, 2)
print(result)

def func2(a, b):
    return a-b
result = func2(2, 1)
print(result)

#Q1
def sum_list(numbers):
    return sum(numbers)
result = sum_list([1, 2, 3, 4])
print(result)

#Q2
def filter_even(numbers):
    return filter(lambda x: x % 2 == 0, numbers)
result = list(filter_even([1, 2, 7, 8, 10, 11]))
print(result)

#Q3
def find_max_value(numbers):
    return max(numbers)
result = find_max_value([1, 3, 6, 8, 10 ,12])
print(result)

#Q4
def count_occurs(lst, item):
    return lst.count(item)
result = count_occurs(['a', 'b', 'c', 'b', 'a', 'a', 'c'], 'a')
print(result)

#Q5
def flatten_list(nested_list):
    return

#Q1
