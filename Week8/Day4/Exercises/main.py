# Exercise 1 : Pets
# Instructions
# Using this code
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Main_Coon(Cat):
    def sing(self, sounds):
        return f'{sounds}'
#Create another cat bread. In order to do so, create a class which inherits from the Cat class.
# Create a few cat instances.
# Create a list called my_cats, which will hold all the created cat instances.
# Create a variable called my_pets. It’s value is an instance of the Pet class.
# Hint : Use the my_cats variable to create the instance.
# Take all the cats for a walk, use the walk method.

cat1 = Bengal("Benito", 2)
cat2 = Chartreux("Penelope", 5)
cat3 = Main_Coon("Bigotes", 3)
my_cats = [cat1, cat2, cat3]
my_pets = my_cats[2]

for cat in my_cats:
    print(cat.walk())

#----------------------------------------------------------------------------------------------
#
# Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value should be another dog called other_dog,
# returns a string stating which dog won the fight. The winner should be the dog with
# the higher run_speed x weight.
#
# Create 3 dogs and run them through your class.
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking.'

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            print(f"{self.name} has won the fight!")
        else:
            print(f"{other_dog.name} has won the fight!")

dog1 = Dog("Sandokan", 4, 5)
dog2 = Dog("Big Fangs", 5, 7)
dog3 = Dog("Crazy Joe", 2, 6)

print(dog3.bark())
print(dog1.run_speed())
dog2.fight(dog1)
dog1.fight(dog3)

#-------------------------------------------------------------------------------------

# Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and
# the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True
#
# play: takes a parameter which value is a few names of other dogs (use *args). The method
# should print the following string: “dog_names all play together”.
#
# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

import random
#
# class Dog:
#     def __init__(self, dog_name, dog_age, dog_weight):
#         self.name = dog_name
#         self.age = dog_age
#         self.weight = dog_weight
#
#     def bark(self):
#         return f'{self.name} is barking.'
#
#     def run_speed(self):
#         return self.weight / self.age * 10
#
#     def fight(self, other_dog):
#         if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
#             print(f"{self.name} has won the fight!")
#         else:
#             print(f"{other_dog.name} has won the fight!")


class PetDog(Dog):
    def __init__(self, dog_name, dog_age, dog_weight, trained=False):
        self.trained = trained
        super().__init__(dog_name, dog_age, dog_weight)

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        print(f"{self.name,', '.join(list(args))} all play together!")

    def do_a_trick(self):
        tricks = [f"{self.name} does a barrel roll.",
                  f"{self.name} stands on his back legs.",
                  f"{self.name} shakes your hand.",
                  f"{self.name} plays dead."]
        print(random.choice(tricks)) if self.trained else print(f"{self.name} is not trained!")


dog1 = PetDog("Big Fangs", 2, 8)
dog2 = PetDog("John Snow", 4, 12)
dog1.train()
dog1.play("Chester", "Crazy Eye", "Punk")
dog2.play("Chester", "Crazy Eye", "Smily", "Punk")
dog1.do_a_trick()
dog2.do_a_trick()



