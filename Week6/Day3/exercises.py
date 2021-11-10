# Exercise 1 : Favorite Numbers
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = {7, 9}
my_fav_numbers.add(2)
my_fav_numbers.add(4 )
print(my_fav_numbers)


#---------------------------------------------------------------------------

# exercise 3
# Print A Range Of Numbers
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.

number = range(0, 30)
list(number)
print(number)

#Ask the user to input a month(1 to 12).
# Display the season of the month received :
#     Spring runs from March (3) to May (5)
#     Summer runs from June (6) to August (8)
#     Autumn runs from September (9) to November (11)
#     Winter runs from December (12) to February (2)


current_month = input('What month is it? use 1-12 to indicate')

seasons = [[12, 1, 2, 'winter'], [3, 4, 5, 'spring'], [6, 7, 8, 'Summer'], [9, 10, 11, 'Autumn']]
month = int(current_month)
for season in seasons:
    print(season)
    print(season[3])
    if month in season:
        print(f'the season of month {current_month} is {season[3]}')

if current_month in seasons:
    print('its winter')

if 5 >= int(current_month) >= 3:
    print('its spring')

print(winter_months[0][-1])
print(winter_months[-1])
winter_months[5]

print('hello world')

my_list = ['hello', 'world', 'toby', ]
data = input('whats my name?')
my_list.append(data)
print(my_list)
item_to_remove = input('what would you like to remove from the list? ')
my_list.remove(item_to_remove)
print(my_list)

my_list = ['hello', 'world', 1, 2, 3, 4, 5]
my_list2 = [43, 456, 789]
print(my_list + my_list2)
my_num = 5
my_second_num = 23
my_num += my_second_num
my_num = my_num + my_second_num

print(my_num)

# Given this list: list1 = [5, 10, 15, 20, 25, 50, 20], find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

# Hint : Look at the index method

list1 = [5, 10, 15, 20, 25, 50, 20]
list1[list1.index(20)] = 200
print(list1)
my_tuple = (5, 6, 7)
num1, num2, num3 = my_tuple
aTuple = (10, 20, 30, 40)
a, b, c, d = aTuple

counter = 0
for number in list1:
    print(f'n is currently equal to: {number}')
    print('hi')
    counter += 1

print('the loop ran ', counter, ' times')
print(number)

import random

num_list = [random.randint(0, 100) for n in range(20)]

print(num_list)

current_low = num_list[0]
for num in num_list:
    print(f'number we are looking at: {num}\ncurrent lowest: {current_low}')
    if current_low > num:
        print('lower, replacing')
        current_low = num

print(current_low)

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print('loop over')

password = ''
while password != 'hello-world-123':
    password = input('What is the top secret password? ')

print('You guessed the right password!')

num = 1
while num <= 10:
    print(num)
    num += 1

while True:
    city = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
    if city in ['quit', 'leave me alone', 'stop']:
        break
    else:
        print("I'd love to go to", city)

print("Goodbye !")

current_number = -1
while current_number <= 9:

    current_number += 1
    if 3 < current_number < 7:  # If the number is between 3 and 7
        continue  # Go back to the beginning of the loop
    print(current_number)

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9}
my_set2 = set(range(54, 67))
print(my_set)
print(my_set2)
my_set.add('hello')
my_set.remove(1)

print(my_set.union(my_set2))
my_set.update(my_set2)
print(my_set)

'''exercise 1'''
my_fav_numbers = {7, 42, }
my_fav_numbers.add(3)
my_fav_numbers.add(56)
friend_fav_numbers = {3, 97, 88}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

'''exercise 3'''
for number in range(0, 20):
    print(number + 1)

'''exercise 4'''
num_list = []

for num in range(3, 10):
    new_num = num / 2

    if str(new_num)[-1] == '0':
        new_num = num // 2

    num_list.append(new_num)
print(num_list)

