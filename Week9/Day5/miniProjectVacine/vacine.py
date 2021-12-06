# Vaccines Management System
#
# You will have to create two classes:

# Human
# Queue
# Here is a description of them:

# 1) Human
# Represents a citizen of the city, it has the following attributes: id_number (str), name (str), age (int), prioritary (bool) and blood_type (str). Its blood type can be “A”, “B”, “AB” or “O”.

# It got no methods.

# 2) Queue
# Represents a queue of humans waiting for their vaccine. It has two attributes, humans, the list containing the humans that are waiting, it is initialized empty.
# This class is useful to manage who will get vaccinated in priority. It has the following methods:

# add_person(self, person) Add a human to the queue, if he is older than 60 years old or a prioritary person, put him at the beginning of the list (at index 0) before every other.
# find_in_queue(self, person) Returns the index of a human in the queue.
# swap(self, person1, person2) Swaps person1 with person2.
# get_next(self) return the next human in the queue, meaning the object at index 0 in the list.
# get_next_blood_type(self, blood_type) Return the first human with this specific blood type.
# sort_by_age(self) Sort the queue so that the older ones are before the younger ones and all the prioritary persons are before the others.
# Every human returned by get_next and get_next_blood_type is removed from the list, those functions return None if there is no one in the list.

# Bonus: Don’t use any of the following built-in methods: list.insert, list.pop, list.index, list.sort, sorted.

# Part 2
# Create an attribute family for the Human class. Initialized as empty, family is a list of all the humans that are living in the same house with this human. Add a method add_family_member(self, person) that adds the person to this human’s family and this human to the person’s family.

# Add the rearange_queue(self) method to the Queue class, so that there is no two members of the same family one after the other.

from typing import AsyncGenerator


class Human:
    def __init__(self, id_number: str, name: str, age: int, priority: bool, blood_type: str) -> None:
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type

    def add_family_member(self, person):
        self.family.append(person)

    def __str__(self):
        return f"name: {self.name} age: {self.age} priority: {self.priority}"


class Queue:
    def __init__(self) -> None:
        self.humans = []

    def add_person(self, person):
        if person.age > 60 or person.priority:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)

    def find_in_queue(self, person):
        for index in range(len(self.humans)):
            if self.humans[index].id_number == person.id_number:
                return index
            return -1

    def swap(self, person1, person2):
        person1_index = self.find_in_queue(person1)
        person2_index = self.find_in_queue(person2)
        self.humans[person1_index] = person2
        self.humans[person2_index] = person1

    def get_next(self):
        return self.humans[0]

    def get_next_blood_type(self, blood_type):
        for human in self.humans:
            if blood_type == human.blood_type:
                return human
        return None

    @staticmethod
    def get_age(human):
        return human.age

    @staticmethod
    def get_priority(human):
        return 1 if human.priority else 0

    def sort_by_age(self):
        self.humans.sort(key=Queue.get_age, reverse=True)
        self.humans.sort(key=Queue.get_priority, reverse=True)

    def __str__(self):
        humans = []
        for index in range(len(self.humans)):
            humans.append(str(self.humans[index]))

        return "\n".join(humans)

    def rearrange_queue(self):
        for i in range(len(self.humans)):
            if self.waiting_humans[i] and self.humans[i + 1] in Human.family:
                self.swap(i + 1, i + 2)


joselyn = Human("0456", "Joselyn", 22, False, "O")
adriel = Human("4567", "Adriel", 19, False, "B")
mary = Human("7834", "Mary", 34, True, "O")
albert = Human("4579", "Albert", 36, False, "B")
shoshana = Human("0987", "Shoshana", 45, True, "AB")
angy = Human("1126", "Angy", 45, True, "O")

queue = Queue()

queue.add_person(albert)
