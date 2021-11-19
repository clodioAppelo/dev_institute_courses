# Instructions
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Suppose the following input is supplied to the program:
# without,hello,bag,world

# Then, the output should be:
# bag,hello,without,world


given_words = input("Please, enter your words separated by a comma: \n")
list_words = given_words.split(" ")
print(list_words)
new_list = sorted(list_words)
print(new_list)
