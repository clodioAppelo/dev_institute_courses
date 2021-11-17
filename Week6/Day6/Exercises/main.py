# Exercise 1 : Convert Lists Into Dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# res = {}
# for key in keys:
#     for value in values:
#         res[key] = value
#         values.remove(value)
#         break
# print("Resultant dictionary is : " + str(res))

#--------------------------------------------------------------------------------------------

# Exercise 2 : Cinemax #2
# Instructions
# “Continuation of Exercise Cinemax from Week4Day2 XP”
#
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# How much does each family member have to pay ?
#
# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable
# (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

# family = {}
# while True:
#     name = input('whats the party members name? if you are done type quit ')
#     if name == 'quit':
#         break
#     age = int(input(f"what's {name}\'s age?" ))
#     family[name] = age
#     family.update({name:age})
#
# total = 0
# for name, age in family.items():
#     if age < 3:
#         continue
#     if 3 <= age <= 12:
#         total += 10
#     if age > 12:
#         total +=15
#
# print(f'the total for the family is {total}')

#------------------------------------------------------------------------------------------------

# Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color:
#     France: blue,
#     Spain: red,
#     US: pink, green
# Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# brand = {"main": {"name": "Zara",
# "creation_date": 1975,
# "creator_name": "Amancio Ortega Gaona",
# "type_of_clothes": "men, women, children, home",
# "international_competitors" : ["Gap, H&M, Benetton"],
# "number_stores": 7000, "major_color": {
#     "France": "blue",
#     "Spain": "red",
#     "US": "pink, green",
#         }
# }}
# 3. Change the number of stores to 2.
# 4. Print a sentence that explains who Zara's clients are.
#print("Zara's clients are : ", brand["main"]["type_of_clothes"])
# 5. Add a key called country_creation with a value of Spain.
#brand.update({"country_creation": "Spain"})
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
## 7. Delete the information about the date of creation.
#del brand["main"]["creation_date"]
# 8. Print the last international competitor.
#print(brand["international_competitors"][3])
# 9. Print the major clothes colors in the US.
#print(brand["main"]["major_color"]["US"])
# 10. Print the amount of key value pairs (ie. length of the dictionary).
#print(brand.values())
# 11. Print the keys of the dictionary.
#print(brand.keys())
# 12. Create another dictionary called more_on_zara with the following details:
# creation_date: 1975
# number_stores: 10 000
#more_on_Zara = {
#     "creation_date": 1975,
#     "number_stores": 10000,
# }
# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# brand.update(more_on_Zara)
# # 14. Print the value of the key number_stores. What just happened ?
# print(brand["number_stores"])
# print(brand)
# print(brand.keys())
# it prints 10000 from nested dictionary more_on_Zara and ignores the 7000 in key located in main

#-----------------------------------------------------------------------------------------------------------

# Exercise 4 : Disney Characters
# Instructions
# Use this list :

users = ["Mickey", "Minnie", "Donald","Ariel","Pluto"]

#Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.

#>>> print(disney_users_A)
#{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
# disney_users_A = {users[i]: i for i in range(0, len(users))}
# print(disney_users_A)

#2/
#>>> print(disney_users_B)
#{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
# disney_users_B = {i: users[i] for i in range(0, len(users))}
# print(disney_users_B)

#3/
#>>> print(disney_users_C)
#{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
# disney_users_C = sorted(users)
# print(disney_users_C)
# disney_users_C = {disney_users_C[i]: i for i in range(0, len(disney_users_C))}
# print(disney_users_C)

