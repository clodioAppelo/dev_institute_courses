# #Daily Challenge:
# Instructions
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
#
# Then, print the first and last characters of the given text.
#
# Construct the string character by character: Print the first character, then the second, then the third,
# until the full string is printed.



user = input("He enter an statement 10 characters long: ")
if len(user) <= 10:
    print("“string not long enough”")
elif len(user) >= 10:
    print("string too long")
else: print(" well done")

print(user[0] + user[-1])

i = 0
while i < len(user):
    i += 1
    print(user[0:i])



