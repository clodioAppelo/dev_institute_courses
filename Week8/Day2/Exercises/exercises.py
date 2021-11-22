# Exercise 1: Cats
# Instructions
# Using this class
#

import string


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate three Cat objects using the code provided above.
cat_a = Cat("GreyClaw", 1)
cat_b = Cat("Snowball", 3)
cat_c = Cat("Euriclides", 2)


# def oldest_cat(cat_a, cat_b, cat_c):
#     oldest = [cat_a.age, cat_b.age, cat_c.age]
#     return max(oldest)
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.


# print(cat_a.name)
# print(cat_a.age)
# print(cat_b.name)
# print(cat_b.age)
# print(cat_c.name)
# print(cat_c.age)
# print(f"The oldest cat is {oldest_cat(cat_a,cat_b,cat_c)} years old.")

# --------------------------------------------------------------------------------------------------------------------

# Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.


class Dogs:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")


davids_dog = Dogs("Rex", 50)
sarahs_dogs = Dogs("Teacup", 20)

# print(
#     f"David's dog's name is {davids_dog.name} and it jumps {davids_dog.height} cm high")
# print(davids_dog.bark())
# print(davids_dog.jump())


# print(sarahs_dogs.name, sarahs_dogs.height)
# sarahs_dogs.bark()
# sarahs_dogs.jump()

# if davids_dog.height > sarahs_dogs.height:
#     print(f"{davids_dog.name} is the is the bigger dog!")
# else:
#     print(f"{sarahs_dogs.name} is the bigger dog!")


# -----------------------------------------------------------------------------------------------------------

# Exercise 3 : Who’s The Song Producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for item in self.lyrics:
            print(item)


stairway = Song(["There’s a lady who's sure", "all that glitters is gold",
                "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

# -----------------------------------------------------------------------------------------------------------

# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Create a method called get_groups that prints the animal/animals inside each group.
# Create an object called ramat_gan_safari and call all the methods.


class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        for item in self.animals:
            print(item)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print("animal not registered at this Zoo")

    def sort_animals(self):
        for letter in list(string.ascii_uppercase):
            animalArray = [
                animal for animal in self.animals if animal.startswith(letter)]
            sortedArray = sorted(animalArray)
            if sortedArray:
                print(animalArray)


ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Emu")
ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Eel")
ramat_gan_safari.get_animals()
ramat_gan_safari.sort_animals()
