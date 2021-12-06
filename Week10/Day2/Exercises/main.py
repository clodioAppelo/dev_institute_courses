# Exercises 1

# import OriginFile
#
# OriginFile.display_name()

#from OriginFile import display_name

#from OriginFile import display_name as ds

#import OriginFile as OF

#------------------------------------------------------------------------------

#Exercise 2

# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.

# import random
#
# def my_random_num(num):
#     ran_num = random.randint(1,101)
#     if num == ran_num:
#         print("That's a match!")
#     else:
#         print("Try again")
#
# my_random_num(67)

#---------------------------------------------------------------------------------------------

# Exercise 3
import random
import string


def Upper_lower_string(length):
    result = ''.join((random.choice(string.ascii_letters) for x in range(length)))
    print(result)


Upper_lower_string(5)
