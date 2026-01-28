"""
syntax 
class ClassName:
    def __init__(self, parameter1, parameter2):
        self.property1 = parameter1
        self.property2 = parameter2

__init__() constructor
self.property:

===============================
Types of constructor
1- default constructor (self)
2- parameterized constructor (self, name, age)
3- constructor with default values (self, name='unknown', age=0)
"""

class car:
    def __init__(self, brand,color):
        self.brand=brand
        self.color=color

car1 = car('tata','black') #values automatically set
print(car1.brand, car1.color)