# Instructions : Old MacDonald’s Farm
# Take a look at the following code and output!
# File: market.py

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())

# output

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!

# Create the code that is needed to recreate the code provided above. Below are a few questions to assist you with your code:
# 1. Create a class called Farm. How should this be implemented?


# 2. Does the Farm class need an __init__ method? If so, what parameters should it take?


# 3. How many methods does the Farm class need?


# 4. Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?


# 5. Test your code and make sure you get the same results as the example above.


# 6. Bonus: nicely line the text in columns as seen in the example above. Use string formatting.

class Farm:

    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, mount=1):
        if animal_type in self.animals:
            self.animals[animal_type] = self.animals[animal_type] + mount
        else:
            self.animals[animal_type] = mount

    def get_animal_types(self):
        #     # This method should return a sorted list of all the animal types (names) in the farm.
        #     # With the example above, the list should be: ['cow', 'goat', 'sheep'].
        return sorted(self.animals.keys())

    def get_info(self):
        print(f"{self.farm_name}'s farm\n")

        for animal_type, animal_mount in self.animals.items():
            print(f'{animal_type}: {animal_mount}')

        return '\n\tE-I-E-I-0!'

    # should return the following string: “McDonald’s farm has cows, goats and sheep.”
    def get_short_info(self):
        # The method should call the get_animal_types function to get a list of the animals.
        animal_list = macdonald.get_animal_types()
        return f"McDonald’s farm has {animal_list[0]}s, {animal_list[1]}s and {animal_list[2]}."

# ----------------------------------------------------------------------------------------


# Expand The Farm
# Add a method called get_animal_types to the Farm class. This method should return a sorted list
# of all the animal types (names) in the farm. With the example above, the list should be:
# ['cow', 'goat', 'sheep'].

# Add another method to the Farm class called get_short_info. This method should return the following string: “McDonald’s farm has cows, goats and sheep.”. The method should call the get_animal_types function to get a list of the animals.
# ------------------------------------------------------------------------------------------

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())



