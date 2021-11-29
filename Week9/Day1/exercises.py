from random import choice, randint


class Circle:
    color = "red"

    def __init__(self, diameter):
        self.diameter = diameter

    def grow(self, factor=2):
        self.diameter = self.diameter * factor

    def get_color(self):
        return Circle.color


circle1 = Circle(2)
print(circle1.color)
print(Circle.color)
print(circle1.get_color())
circle1.grow(3)
print(circle1.diameter)

# ----------------------------------------------------


class MyClass(object):
    count = 0

    def __init__(self, val):
        self.val = val
        MyClass.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    @classmethod
    def get_count(cls):
        return cls.count


object_1 = MyClass(10)
print("\nValue of object : %s" % object_1.get_val())
print(MyClass.get_count())

object_2 = MyClass(20)
print("\nValue of object : %s" % object_2.get_val())
print(MyClass.get_count())

# ------------------------------------------------------------------------------------


class MyClass(object):
    count = 0

    def __init__(self, val):
        self.val = self.filterint(val)
        MyClass.count += 1

    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            print("Entered value is not an INT, value set to 0")
            return 0
        else:
            return value


a = MyClass(5)
b = MyClass(10)
c = MyClass(15)

print(a.val)
print(b.val)
print(c.val)
print(a.filterint(100))

# --------------------------------------------------------------------------------


class Racecar():
    def __init__(self, model, reg_no, top_speed=0, nitros=False):
        self.model = model
        self.reg_no = reg_no
        self.top_speed = top_speed
        self.nitros = nitros

        if self.nitros:
            self.top_speed += 50

    def __str__(self):
        return self.model.capitalize()

    def __repr__(self):
        return f"This is a Racecar with registration: {self.reg_no}"

    def __call__(self):
        print(f"Vroom Vroom. The {self.model} Engines Started")

    def __gt__(self, other):
        if self.top_speed > other.top_speed:
            return True
        else:
            return False

    def drive(self, km):
        print(
            f"You drove the {self.model} {km} km in {km / self.top_speed} hours.")

    def race(self, other_car):
        if self > other_car:
            print(f"I am the winner")
        else:
            print(f"The {other_car.model} is the winner")


class PrintList():

    def __init__(self, my_list):
        self.mylist = my_list

    def __repr__(self):
        return str(self.mylist)


printlist = PrintList(["a", "b", "c"])
print(printlist.__repr__())
printlist

# ----------------------------------------------------------------------------------------------


class Dog:

    def __init__(self, name, age, weight, breed, gender):
        self.name = name
        self.age = age
        self.weight = weight
        self.breed = breed
        self.gender = gender

    def __str__(self):
        return "I'm a DOG called " + self.name

    def __repr__(self):
        return f"Dog: name = {self.name}"

    def __len__(self):
        if breed == "dachshund":
            return self.weight * 5
        else:
            return self.weight * 3

    def __gt__(self, other):
        return "All dogs are created equal"

    def __ge__(self, other):
        return self.age >= other.age

    def __add__(self, other):
        if self.gender == other.gender:
            return None
        if self.breed != other.breed:
            breed = self.breed + "-" + other.breed
        else:
            breed = self.breed
        age = 0
        weight = (self.weight + other.weight)/20
        return [Dog(f"Puppy {i+1}", age, weight, breed, choice(["M", "F"])) for i in range(randint(1, 6))]

    def __mul__(self, other):
        return self.__add__(other)
