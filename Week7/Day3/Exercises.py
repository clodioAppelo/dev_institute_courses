# def say_hello():
#     """A function that says hello"""
#     print("Hello!")
#     user_string = input('what string would you like duplicated?')
#     print(user_string * 8)

# def say_hello(username, language="EN"):
#     my_name = username
#     if language == "EN":
#         print("Hello ", username)
#     elif language == "FR":
#         print("Bonjour ", username)
#     else:
#         print("This language is not supported: " + language)

# ------------------------------------------------------------------------------------------------------------


# def to_power_of(num):

#     return 4 ** 4

# ---------------------------------------------------------------------------------------

# def split_name(full_name):
#     name_list = full_name.split()
#     return name_list[0], name_list[-1]

# ---------------------------------------------------------------------------------------

# say_hello("Rick", "FR")
# say_hello('Morty')
# say_hello(language='DE', username='Rick')
# say_hello('Toby')
# say_hello(3)
# say_hello([1,2,3,4,5,6])

# ---------------------------------------------------------------------------------

# result = to_power_of(4)
# my_list = [4,3,56,777,1,23,78]
# my_list_sorted = sorted(my_list)

# -------------------------------------------------------------------------------

# print(id(my_list))
# my_list.sort()
# print(id(my_list_sorted))
# print(id(my_list))

# first_name ,last_name = split_name('rick sanchez')
# print(first_name.title(), last_name.title())

# def calculation(a, b):
#     return a + b, a - b

# res = calculation(40, 10)
# print(res)

# def greet_users(users):             # users should be a list
#     for user in users:              # Because it's a list, we can loop through it
#         print("Hello " + user.title() + "!")       # For each user, print "hello" and then his name


# def my_f1():
#     print("Hello")

# def my_f2():
#     print("Word")

# def my_f3():
#     print("This is Rick!")

# my_functions = [my_f1, my_f3, my_f2]
# for func in my_functions:
#     func()

# --------------------------------------------------------------------------------------------------

import random


def print_models(unprinted_designs, completed_models):
    """    
    Simulate printing each design until none are left.    
    Move each design to completed_models after printing.    
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """
    Show all the models that were printed.
    """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


global_scope_design_list = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(global_scope_design_list, completed_models)
print(global_scope_design_list)
show_completed_models(completed_models)

'''
    Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
    Call the function, and make sure the message displays correctly.
'''


def display_message():
    '''this function says what i do in this course'''
    print('im learning python & web dev')


display_message()


'''Create a function that accepts a number between 1 and 
100 and generates another number randomly between 1 and 100.
Compare the two numbers, if it's the same number, 
display a success message, otherwise show a fail message and display both numbers.'''


def hit_or_miss(user_num):

    computer_num = random.randint(0, 100)

    try:
        user_num = int(user_num)
        2/0
    except ZeroDivisionError:
        print('you probably want to use a number, because you dodnt we\'re using the number 10')
        user_num = 10

    if computer_num > user_num:
        print('success, you guessed correctly')
    else:
        print(f'you guessed {user_num}, the correct choice is: {computer_num}')


hit_or_miss('45')
hit_or_miss('23')
hit_or_miss('8')
hit_or_miss('hello')


strings = ['hello', 'world', 'age']

my_dict = {
    'first_name': 'john',
    'last_name': 'cooper',
    'age': 23
}

for string in strings:
    try:
        print(my_dict[string])

    except KeyError:
        print('that key wasnt found')

    except ValueError:
        pass
