# l1=[1, 2, 3, 4, 5, 6]
# l1.insert(2, 6)
# print(l1)
#
# l2 = [1, 2, 3, 4, 5, "a", "a", "b", 1, 2, 4]
# s = l2.count(4)
# print(s)
#
# a = ["b", "g", "a", "d", "f", "c", "h", "e"]
# x = sorted(a)
# print("a after sorted function")
# print(a)
# print(x)
# b = [1, 2, 5, 8, 3]
# b.sort()
# print(b)
#
# lst = [1, 2, 3, 4, 5, 6, 7]
# print(lst[0:4])
# print(lst[::])
# print(lst[::-1])

# Adding Elements In Tuple
# There is no append function in a tuple, but there is an indirect way of
# adding elements into the function:
#
# t1 = (1, 2, 3, 4, 5)
# t2 = (6, 7, 8, 9)
# t3 = t1 + t2
# print(t3)

# Deleting Elements In A Dictionary
# pop() deletes certain key in the dictionary
# popitem() deletes the last element in the dictionary
# clear() erases all the key-value pairs in the dictionary
# cubes = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
# print(cubes.pop(4))
# print(cubes)
# print(cubes.popitem())
# print(cubes)
# cubes.clear()
# print(cubes)
# Accessing Elements In A Dictionary
# key() is used to access the key values in a dictionary
# values() is used to access the values of dictionary
# items() is used to access the key-value pair
# d = {1:'10', 2:'20', 3:'30', 4:'40', 5:'50'}
# l1 =list(d.keys())
# print("the key values are:")
# print(l1)
# l2 = list(d.values())
# print("The values are of dictionary is")
# print(l2)
# l3 = list(d.items())
# print("the list items are")
# print(l3)
#

# Sets
# A set is a collection that is unordered and unindexed. Sets are written with c
#     urly brackets in Python. Sets do not contain repetitive elements.
# The Membership operator is used to check if the element is present or not.
# The remove() function removes certain elements in the set.
# set1 = {1, 2, 3, 4, "hi", "world", "python"}
# print("python" in set1)
# set1.remove(4)
# print(set1)
#
#
# a = {1, 2, 3, 4, 5}
# b = {2, 3, 6, 7, 5}
# c = a^b
# print(c)
# d = a - b
# print(d)
# e = b - a
# print(e)

#Lambda

# Examples Of Simple Lambdas
# Here are a few examples of lambdas in action:
#
# A Squaring Function
# A squaring lambda function
# square = lambda n : n*n
# num = square(5)
# print (num)
# A Subtraction Function
# A subtraction lambda function with multiple arguments
# sub = lambda x, y : x-y
# print(sub(5, 3))


# The Purpose Of Lambdas
# A lambda is much more readable than a full function since it can be written in-line. Hence,
# it is a good practice to use lambdas when the function expression is small.
#
# The beauty of lambda functions lies in the fact that they return function objects.
# This makes them helpful when used with functions like map or filter which require function
# objects as arguments.
#
# Map With Lambda
# A lambda makes the map function more concise.
#
# Lambda:

# myList = [10, 25, 17, 9, 30, -5]
# # Double the value of each element
# myList2 = map(lambda n : n*2, myList)
# print(myList2)
#Normal:

# The code is longer!

# def double(n):
#   return n * 2

# myList = [10, 25, 17, 9, 30, -5]

# myList2 = map(double, myList)
# print (myList2)


# Filter With Lambda
# Similar to map, lambdas can also simplify the filter function.
#
# Lambda:

# myList = [10, 25, 17, 9, 30, -5]
# Filters the elements which are not multiples of 5
# myList2 = filter(lambda n : n%5 == 0, myList)
# print (myList2)
#Normal:

# The code is longer!

# def multipleOf5(n):
#   if(n % 5 == 0):
#     return n
#
# myList = [10, 25, 17, 9, 30, -5]
#
# myList2 = filter(multipleOf5, myList)
# print (myList2)

#---------------------------------------------------------------------------------------

#Funtions

# Exercise
# Write a function calculation() such that it can accept two variables and calculate
# the addition and subtraction of it. And also it must return both addition and subtraction in
# a single return call
#
# For example:
#
# def calculation(a, b):
    # Your Code

# res = calculation(40, 10)
# print(res)


def calcutation(a,b):
    #function returns additions and subtractions
    add = a + b
    subtr = a - b
    print(f"The Result of the addition is: {add}\n and the subtraction is: {subtr}")

calcutation(40, 10)

