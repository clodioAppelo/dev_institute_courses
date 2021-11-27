'''
Part 1 : Quizz :
Answer the following questions

What is a class?
A class is a blue print or a prototype for an object or many objects of that type.

What is an instance?
it is a single and unique unit of a class.

What is encapsulation?
It  is the packing of data and functions that work on that data within a single object. By doing so, you can hide the internal state of the object from the outside. A class is an example of encapsulation. A class bundles data and methods into a single unit.

What is abstraction?
An abstraction is used to hide the irrelevant data/class in order to reduce the complexity. It also enhances the application efficiency. 
What is inheritance?
Inheritance refers to defining a new class with little or no modification to an existing class. The new class is called derived (or child) class and the one from which it inherits is called the base (or parent) class.

What is multiple inheritance?
A class can be derived from more than one base class in Python. This is called multiple inheritance. In multiple inheritance, the features of all the base classes are inherited into the derived class. The syntax for multiple inheritance is similar to single inheritance.

What is polymorphism?
Polymorphism in python defines methods in the child class that have the same name as the methods in the parent class. In inheritance, the child class inherits the methods from the parent class. Also, it is possible to modify a method in a child class that it has inherited from the parent class.

What is method resolution order or MRO?
The Python Method Resolution Order defines the class search path used by Python to search for the right method to use in classes having multi-inheritance. The algorithm change is also refered as old classes and new classes MRO algorithm.
'''

# ---------------------------------------------------------------

# Part 2: Create A Deck Of Cards Class.
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.
import random


class Card:
    def __init__(self, suit, val) -> None:
        self.suit = suit
        self.value = val

    def show(self):
        print(f"{self.value} of {self.suit}")


class Deck:
    def __init__(self) -> None:
        self.cards = []
        self.build()

    def build(self):
        for s in ["hearts", "Diamonds", "Clubs", "Spades"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def Show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def deal(self):
        return self.cards.pop()


deck = Deck()
deck.shuffle()


card = deck.deal()
card.show()
