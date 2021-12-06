# Exercise 1
# Create a class Human, it has the following attributes:

# name (str)
# age (int)
# living_place (Building - Default is None)
# Create another class Building, it has the following attributes:

# address (str)
# inhabitants (List of Human objs - Default is empty)
# Create a class City, it has the following attributes:

# name (str)
# buildings (List of Building objs - Default is empty)
# Add the move(self, building) method to the Human class, it sets the living place of this human to the building and add this human to the building inhabitants.
# Add the construct(self, address) method to the City class, it adds a building at the referenced address.
# Add the info(self, address) method to the City class, it displays the number of buildings and the mean age of the citizens.

from typing import List


class Human:
    def __init__(self, name: str, age: int, living_place=None):
        self.name = name
        self.age = age
        self.living_place = living_place

    def move(self, building):
        # remove from the current bldg.
        # if self.living_place != None:
        if self.living_place:
            self.living_place.remove_inhabitants(self)

        self.living_place = building
        building.inhabitants.append(self)


class Building:
    def __init__(self, address: str, inhabitants: List[Human]):
        self.address = address
        self.inhabitants = inhabitants

    def remove_inhabitants(self, inhabitants: Human):
        self.inhabitants.remove(inhabitants)

    def show_inhabitants_info(self):
        for inhabitant in self.inhabitants:
            print(inhabitant.name, inhabitant.age)

    def get_total_ages_of_humans():
        return len(self.inhabitants)

    def get_total_ages_of_inhabitants(self):
        total_ages = 0

        for inhabitant in self.inhabitants:
            total_ages += inhabitant.age

        return total_ages


class City:
    def __init__(self, name: str, building: List[Building]):
        self.name = name
        self.building = building

    def construct(self, address):
        new_building = Building(address, [])
        self.building.append(new_building)

    def info(self, address):
        counter = 0
        total_ages_of_humans = 0
        number_of_humans = 0

        for building in self.building:
            if building.address == address:
                counter += 1
                number_of_humans = building.building.get_number_of_inhabitants()
                total_ages_of_humans += building.get_total_ages_of_inhabitants()

                mean = total_ages_of_humans / number_of_humans

                print(
                    f"the number of the building at the address{address} ic {counter}")
                print(
                    f"The mean of the age of citizens at the address {address} is {mean}")


jen = Human("Jen", 28)
adriel = Human("Adriel", 18)
mary = Human("Mary", 38)
jhon = Human("Jhon", 42)

building1 = Building("12446 NE 15 Ave", [])
building2 = Building("1245Washington Rd", [])
building1 = Building("12446 NE 15 Ave", [])
building2 = Building("1245Washington Rd", [])

jen.move(building1)
adriel.move(building1)
mary.move(building2)
jhon.move(building2)

tlv = City("TLV", [building1, building2, building2])
tlv.info("st")

print(building1.inhabitants)
building1.show_inhabitants_info()
jen.move(building1)
