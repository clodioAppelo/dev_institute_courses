# Exercise 1 : What Are You Learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

# def display_message():
#     print("Hi, I am learning functions in Python")


# display_message()

# ------------------------------------------------------------------------------------------------------------
# Exercise 2: What’s Your Favorite Book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as “One of my favorite books is Alice in Wonderland”.
# Call the function, make sure to include a book title as an argument when calling the function.


# def favorite_book(title):
#     print("One of my favorite books is: ", title)


# favorite_book("The lord of the rings")
# --------------------------------------------------------------------------------------------------------------

# Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as “Reykjavik is in Iceland”.
# Give the country parameter a default value.
# Call your function.


# def describe_city(city, country):
#     print(f"{city} is in {country}")


# describe_city("Buenos Aires", "Argentina")

# -----------------------------------------------------------------------------------------------------------

# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

# def Compare_numbers(num):
#     import random
#     rand = random.randint(0, 100)
#     if rand == num:
#         print("We have a Match!")
#     else:
#         print("you have failed, try again!")


# Compare_numbers(7)

# -----------------------------------------------------------------------------------------------------------

# Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function make_shirt() using positional arguments to make a shirt.
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
# Bonus: Call the function make_shirt() using keyword arguments.

# def make_shirt(size, text):
# def make_shirt(text):
#     print(f"This T-shirt is size Large, {text}")


# make_shirt("I love Python!")

# def make_shirt(size):
#     if size == "large" or size == "medium":
#         print("I love Python")
#     else:
#         print("I love River Plate")


# make_shirt("large")
# make_shirt("midium")
# make_shirt("small")

# def make_shirt(size, text):
#     size == print(f"This T Shirt is size {size}, {text}")


# make_shirt("large", "I love Python")
# make_shirt("midium", "I love River Plate")
# make_shirt("small", "Am Israel Chai")

# --------------------------------------------------------------------------------------------------------------

# Exercise 6 : Magicians …
# Instructions
# Make a list of magician’s names.
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great"
# to each magician’s name.
# Call the function make_great().
# Call the funcyion show_magicians() to see that the list has actually been modified.

magician = ["Harry Potter", "Mago Cacarulo", "David Copperfield", "Merlin"]


def Show_magicians():
    for item in magician:
        print(item)


Show_magicians()


def make_great():
    for item in magician:
        print(f"'the Great {item}'")


make_great()
