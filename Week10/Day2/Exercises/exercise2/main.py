# Exercise_XP_2

# Exercise 1
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.

# from datetime import datetime
#
# print(datetime.date(datetime.now()))

#------------------------------------------------------------------------------

# Exercise 2
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).


# import datetime

# date_now = datetime.datetime.now()
# jan_1 = datetime.datetime(2022,1,1)
# time_left = jan_1 - date_now
# print(f"{time_left} till New years!")

#----------------------------------------------------

# Exercise 3
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice),
# then display a message stating how many minutes the user has been alive.

import datetime

# def time_alive(year, month, day):
#     birthday = datetime.datetime(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")))
#     now = datetime.datetime.now()
#     difference = now - birthday
#     print(f"You've been alive for {difference}")
#
# time_alive(1972, 3, 7)


#-----------------------------------------------------------------------------------------

# Exercise 4
# Instructions
# Write a function that display today’s date.
# The function should also display the amount of time left from now until the next upcoming holiday
# and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
# Hint: Start by hard coding the datetime and name of the upcoming holiday.

# import datetime
#
# def next_holiday():
#     now = datetime.datetime.today()
#     next_holiday = datetime.datetime(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")))
#     difference = next_holiday - now
#     print(f"Today's date is {now}\nand the next holiday is in {difference}")
#
# next_holiday()

#---------------------------------------------------------------------------------------------------
# Exercise 5 : How Old Are You On Jupiter?
# Instructions
# Given an age in seconds, calculate how old someone would be on:
# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you are told someone is 1,000,000,000 seconds old, the function should output that they
# are 31.69 Earth-years old.


# age = int(input("How old are you? "))
# years_in_sec = age * (365*24*60*60)
# print("your age in seconds is: ",years_in_sec)
# earth = years_in_sec / 31557600
# mercury = earth * 0.2408467
# venus = earth * 0.61519726
# mars = earth * 1.8808158
# jupiter = earth * 11.862615
# saturn = earth * 29.447498
# uranus = earth * 84.016846
# neptune = earth * 164.79132
#
# print(f"You are {round(earth, 2)} Earth-years old.")
# print(f"You are {round(venus, 2)} Venus-years old")
# print(f"You are {round(mars, 2)} Mars-years old")
# print(f"You are {round(jupiter, 2)} Jupiter-years old")
# print(f"You are {round(saturn, 2)} Saturn-years old")
# print(f"You are {round(uranus, 2)} Uranus-years old")
# print(f"You are {round(neptune, 2)} Neptune-years old")


#---------------------------------------------------------------------------------------------

# Exercise 6 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement
# faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following
# keys: name, adress, langage_code. Use faker to populate them with fake data.
from faker import Faker
fake = Faker()


def add_new_dict():
    user = {}
    user['name'] = fake.name()
    user['address'] = fake.address()
    user['language code'] = fake.language_code()
    users.append(user)


add_new_dict()
add_new_dict()
add_new_dict()
for user in users:
    print(user)
users = []
