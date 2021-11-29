# Exercise 1 : Built-In Functions
# Instructions
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.

# Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.


# Returns absolute value.
transaction_Change = -20.35
print(f"Absolute value of Change Back is: {abs(transaction_Change)}")

# Converts this value into an integer.
print(f"int(50.25) is: {int(50.25)}")

# user input
user_name = input("Please enter your name : ")
print(user_name)
user_age = input("Enter your age : ")
print(user_age)

# __doc__ provides a documentation of the object.


class AmericanFootballTeam:
    """My Favorite Team  is Seattle Seahawk."""

    def do_not_do_anything(self):
        pass


print(AmericanFootballTeam.__doc__)

# ----------------------------------------------------------------------------------------------------------------

# Exercise 2: Currencies
# Instructions
# Create the code which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

#
# >>> str(c1)
# '5 dollars'

# >>> int(c1)
# 5

# >>> repr(c1)
# '5 dollars'

# >>> c1 + 5
# 10

# >>> c1 + c2
# 15

# >>> c1
# 5 dollars

# >>> c1 += 5
# >>> c1
# 10 dollars

# >>> c1 += c2
# >>> c1
# 20 dollars

# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>


# class Currency:
#     def __init__(self, currency: str, value: int):
#         self.currency = currency
#         self.value = value

#     def __str__(self):
#         return f"{self.value} {self.currency}"

#     def __int__(self):
#         return self.value

#     def __repr__(self):
#         return f"{self.value} {self.currency}"

#     def __add__(self, another):
#         if isinstance(another, int):
#             return Currency(self.currency, (self.value + another))
#         elif isinstance(another, Currency):
#             if another.currency is not self.currency:
#                 raise TypeError(
#                     f"Cannot add between Currency type {self.currency} and {another.currency}")
#             else:
#                 return Currency(self.currency, (self.value + another.value))


# c1 = Currency("dollar", 5)
# c2 = Currency("dollar", 10)
# c3 = Currency("shekel", 1)
# c4 = Currency("shekel", 10)

# print(str(c1))

# print(int(c1))

# print(repr(c1))

# print(c1 + 5)

# print(c1 + c2)

# print(c1)

# c1 += 5
# print(c1)

# print(c1 + c3)
