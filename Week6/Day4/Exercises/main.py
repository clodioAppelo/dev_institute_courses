# # Exercise 1
# # Instructions
# # Create a set called my_fav_numbers with all your favorites numbers.
# # Add two new numbers to the set.
# # Remove the last number.
# # Create a set called friend_fav_numbers with your friend’s favorites numbers.
# # Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

# my_fav_numbers = {7, 3}
# my_fav_numbers.add(9)
# my_fav_numbers.add(44)
# print(my_fav_numbers)
# my_fav_numbers.remove(44)
# friend_fav_numbers = {3, 97, 88}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

#----------------------------------------------------------------------------------------------

# Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

# Tuples are immutable

#--------------------------------------------------------------------------------------------

#Exercise 3: Print A Range Of Numbers
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.

# for number in range(0, 20):
#     print(number+1)
#----------------------------------------------------------------------------------------------

#Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5
# (don’t hard-code the sequence).

# an integer is a whole number while a float is a decimal

# num_list = []
#
# for num in range(3, 10):
#     new_num = num / 2
#
#     if str(new_num)[-1] == '0':
#         new_num = num // 2
#
#     num_list.append(new_num)
# print(num_list)

#----------------------------------------------------------------------------------------------

#Exercise 5: Shopping List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
#
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

# list_baskets = ["Banana", "Apples", "Oranges", "Blueberries"]
# list_baskets.pop(0)
# list_baskets.pop()
# list_baskets.append("Kiwi")
# list_baskets.insert(0, "Apples")
# print(list_baskets)
# apples_count = list_baskets.count("Apples")
# print(apples_count)
# list_baskets.clear()
# print(list_baskets)

#---------------------------------------------------------------------------------------

#Exercise 6 : Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input
# is equal to your name.
# name = " "
# while name !="claudio":
#     name = input("Hi, whats your name?: ").lower()
# print("Congratilations my name is also 'Claudio' ")

#-----------------------------------------------------------------------------------------
# Exercise 7
# Instructions
# Exercise 7
# Instructions
# Given a list, use a loop to print out every element which has an even index.

# my_list = [2, 5, 6, 8, 9, 10]
# even_i = []
#
# for i in my_list:
#     if i % 2 == 0:
#         even_i.append([i])
#
# print(even_i)

#----------------------------------------------------------------------------------------

#Exercise 8
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7
# multiples=[]
# for i in range(1500, 2500):
#     if (i % 7 == 0) and (i % 5 == 0):
#         multiples.append(str(i))
# print(','.join(multiples))

#------------------------------------------------------------------------------------------
# Exercise 9: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space,
# eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits!
#  Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

# user_fruits = input("Please enter fruits separated with a single space: ").lower()
# fruits_list = user_fruits.split()
# print(fruits_list)
# name = [input(" what's your favorite fruit? ").lower()]
#
# if any(name[0] in word for word in fruits_list):
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")

#------------------------------------------------------------------------------------------------

#Exercise 10: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop
# asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is
# (10 + 2.5 for each topping).
# looping = True
# list_topping = []
#
# while looping:
#     pizza_topping = input("Hi, enter the pizza topping you want to add: ").lower()
#     if pizza_topping == "quit":
#         looping = False
#         topping_cost = len(list_topping) * 2.5
#         print("Your Total Amount is : ", 10 + topping_cost)
#     else:
#         list_topping.append(pizza_topping)
#         print("What else do you want on your pizza? ")
#


#-----------------------------------------------------------------------------------------------

# Exercise 11: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.
# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted
# for people between the ages of 16 and 21.
# Write a program that asks every user for their age, and prints a list of the teens who
# are permitted to watch the movie.

# prompt = input(" Hi how old are you? --Enter quit to finish: ")
#
# ticket_cost = 0
# while True:
#     age = input(prompt)
#     if age == "quit":
#         break
#
#     age = int(age)
#     if age < 3:
#         print("your ticket is Free!")
#         ticket_cost += 0
#     elif age < 13:
#         print("your ticket is $10")
#         ticket_cost += 10
#     else:
#         print(" Your ticket is $15")
#         ticket_cost += 15
#     print(f"your total is: {ticket_cost}")
#
# teenager = []
# while True:
#     name = input("What is your name? type quit when you are done")
#     if name == "quit":
#         break
#     age = int(input("how old are you? "))
#     if age > 21:
#         teenager.append(name)
#     print(f"You {teenager} can watch this movie ")


#--------------------------------------------------------------------------------------------------------

# Exercise 12 : Who Is Under 16?
# Instructions
# Given a list of names, write a program that asks every user for their age, if they are less
# than 16 years old remove them from the list.
# At the end, print the final list.

# names = ["Charly", "joe", "Avi", "Claudio"]
# for name in names:
#     age = int(input(f"Hello {name}, How old are you? ))
#     if (age <= 16):
#         names.remove(name)
# print(names)

#--------------------------------------------------------------------------------------------------

# Exercise 13
# Instructions
# Make a list called sandwich_orders and fill it with the names of various sandwiches .
# Then make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made,
# such as I made your tuna sandwich.

# sandwich_orders = ["Tuna", " Chicken", "Salmon", "Vegan"]
# ready_sandwiches = []
#
# while sandwich_orders:
#     current_sand = sandwich_orders.pop()
#     print("I am working on your" + current_sand + "Sandwich.")
#     ready_sandwiches.append(current_sand)
# print("\n")
# for sandwich in ready_sandwiches:
#     print("your" + sandwich +" Sandwich is ready")
#--------------------------------------------------------------------------------------------

#Exercise 14
# Instructions
# Using the list sandwich_orders from Exercise 13, make sure the sandwich ‘pastrami’ appears in
# the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of
# pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ["Pastrami","Tuna", "Pastrami"  "Chicken", "Salmon", "Vegan", "Pastrami"]
ready_sandwiches = []

print("We are sorry to tell you we ran out of Pastrami")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
    print(sandwich_orders)

while sandwich_orders:
    current_sand = sandwich_orders.pop()
    print("I am working on your" + current_sand + "Sandwich.")
    ready_sandwiches.append(current_sand)

print("\n")
for sandwich in ready_sandwiches:
    print("your" + sandwich + " Sandwich is ready")




