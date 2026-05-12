""" OBJECTS
(1) what is an object?
(2) Iterable objects and rang
(3) Dictionaries
(4) Error handling system
"""

import array  # Package or module
import math
from math import ceil, asin  # method
print("=======what is an object?========")
# An obj has state and methods properties
# everything in python is an object

print(type("Hello world"))  # str class
print(type(42))  # int class
print(type(3.14))  # float class
print(type(True))  # bool class
print(type(array))  # list class
print(type(math))  # module class

# Paradigm >> Object Oriented Programming (OOP)
# OOP 4 concepts >> Encapsulation, Abstraction, Inheritance, Polymorphism
result1 = math.ceil(3.77)  # ceil method  4 chiqaradi javobni
print(result1)
result2 = asin(0.5)  # asin method  0.5235987755982989 chiqaradi javobni
print(result2)
