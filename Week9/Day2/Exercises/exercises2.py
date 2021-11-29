# Exercise 1 : Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]
# Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# a method that prints all the members of the family.

class Family:
    def __init__(self, last_name: str):
        self.members = [{'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
                        {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}]
        self.last_name = last_name

    def born(self, **kwargs):
        new_member = {}
        for key, value in kwargs.items():
            new_member[key] = value
        self.members.append(new_member)
        print("Matzal Tov! on your new addition to the family!")

    def is_18(self, name):
        for member in self.members:
            if name in member['name'] and member['age'] >= 18:
                return True
            else:
                return False

    def print_all_members(self):
        for member in self.members:
            print(member['name'])


# family1 = Family("Bender")
# family1.print_all_members()
# family1.born(name="Yair", age=0, gender="Male", is_child=True)
# family1.print_all_members()
# print(family1.is_18("Yair"))

# -------------------------------------------------------------------------------------------------------------

# Exercise 2 : TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.

# Add a method called use_power, this method should print the power of a member if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.

# Add a method called incredible_presentation which presents the family members with their incredible names and powers.

# Look up the names of The Incredibles characters on Google and build the family (if you can’t find the correct information just improvise).
# Print their normal presentation and their incredible presentation.
# Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
# Print both presentations again. Check that Baby Jack is born and that his power is showing when using the incredible representation.


class TheIncredibles(Family):
    def __init__(self, last_name: str):
        self.last_name = last_name
        self.members = [{'name': 'Robert', 'age': 40, 'gender': 'Male', 'is_child': False, 'power': 'Superhuman strength,stamina,durability', 'incredible_name': 'Mr.Incredible'},
                        {'name': 'Helen', 'age': 38, 'gender': 'Female', 'is_child': False,
                            'power': 'Elasticity', 'incredible_name': 'Elastigirl'},
                        {'name': 'Violet', 'age': 14, 'gender': 'Female', 'is_child': True,
                            'power': 'Force field,Invisibility', 'incredible_name': 'Violet'},
                        {'name': 'Dash', 'age': 10, 'gender': 'Male', 'is_child': True, 'power': 'Superspeed', 'incredible_name': 'Dash'}]

    def use_power(self):
        for member in self.members:
            if member['age'] >= 18:
                print(member['name'])
            raise Exception(f"{member['name']} is not 18 years old yet!")

    def incredible_presentation(self):
        for member in self.members:
            print(
                f"This is {member['incredible_name']} and his/her power is {member['power']}")


family2 = TheIncredibles("Parr")
family2.print_all_members()
family2.born(name='Jack', age='1', gender='Male', is_child=True,
             power='unknown', incredible_name='Jack Jack')
family2.print_all_members()
family2.incredible_presentation()
