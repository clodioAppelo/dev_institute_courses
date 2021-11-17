# Instructions
# Write a function to compute 5/0 and use try/except to catch the exceptions.
# Bonus : use some Buit-in exceptions of Python


def try_except_function(a, b, i):
    '''Try and except function'''
    try:
        sum = a / b
        print(sum)
        my_list = [1, 2, 3, 4, 5, 6]
        i = my_list[i]

    except ZeroDivisionError:
        print(" I cannot divide by Zero")
    except IndexError:
        print("Index cannot be greater than size of list")
    finally:
        print("This block will be always excecuted even though exception is not excecuted")


try_except_function(5, 0, 8)
