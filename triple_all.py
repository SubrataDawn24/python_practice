"""
# 1. Write a Python program to triple all numbers of a given list of integers. Use Python map.

List = {12,5,9,6,18,21,3}
cube_list=map(lambda x:(x*3),List)
print(cube_list)

Return double of n
def addition(n):
	return n + n

# Write a Python program to square the elements of a list using map() function.
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# Write a Python program to add two given lists and find the difference between lists. Use map() function.
def square(n):
    return n*n
numbers = (1,2,3,4)
result = map(square, numbers)
print(list(result))

list1=[1,2,3,4]
list2=[4,3,2,1]
li=list(map(lambda x,y:x+y,list1,list2))
print(li)


Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(subject_marks)


# Write a Python program to sort a list of dictionaries using Lambda. Go to the editor
phone=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print("Orignal dictionary:")
print(phone)
phone.sort(key = lambda x: x['model'])
print("sorted dict")
print(phone)


# fibonacci series
from functools import reduce

fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
								range(n-2), [0, 1])

print(fib(10))

from functools import reduce
 
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                range(n-2), [0, 1])
 
print("Fibonacci series upto 2:")
print(fib_series(2))
print("\nFibonacci series upto 5:")
print(fib_series(5))
print("\nFibonacci series upto 6:")
print(fib_series(6))
print("\nFibonacci series upto 9:")
print(fib_series(9))

python code to demonstrate working of reduce()

importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

def my_add(a, b):
   result = a + b
   print(f"{a} + {b} = {result}")
   return result


my_add(5, 5)


from functools import reduce
numbers = [0, 1, 2, 3, 4]
reduce(my_add, numbers)

def num(n):
    return lambda x: x*n
i=int(input("enter the  input:"))
result =num(2)
print(f"double the number of: {i}: ",result(i))
result =num(3)
print(f"double the number of: {i}: ",result(i))
result =num(4)
print(f"double the number of: {i}: ",result(i))
result =num(5)
print(f"double the number of: {i}: ",result(i))
"""
