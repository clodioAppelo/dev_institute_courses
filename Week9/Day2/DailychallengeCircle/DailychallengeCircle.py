# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the circle and get something nice
# Be able to add two circles together
# Be able to compare two circles to see which is bigger
# Be able to compare two circles and see if there are equal
# Be able to put them in a list and sort them

class Circle:
    circles = []

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return int(self.radius**2*3.14)

    def add_circles(self, new_cir):
        result = self.area() + new_cir.area()
        print(f"The sum of the two circles together is {result}")

    def if_bigger(self, new_cir):
        if self.area() > new_cir.area():
            print(f"{self.area()} is the area of the bigger circle.")
        else:
            print(f"{new_cir.area()} is the area of the bigger circle.")

    def if_equal(self, new_cir):
        if self.area() == new_cir.area():
            print(f"The two circles are equal.")
        else:
            print(f"The two circles are not equal.")

    def put_in_list(self):
        self.circles.append(self)
        self.circles.sort(key=Circle.area)
        for item in self.circles:
            print(item.area())


circle1 = Circle(10)
circle2 = Circle(5)
print(circle1.area())
print(circle2.area())
circle1.add_circles(circle2)
circle2.if_bigger(circle1)
circle1.if_equal(circle2)

circle3 = Circle(2)
circle4 = Circle(12)

circle1.put_in_list()
circle2.put_in_list()
circle3.put_in_list()
circle4.put_in_list()
