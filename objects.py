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

print("=======Error handling system========")

car_dict = dict(make="Toyota", model="Camry", year=2020, electric=False)

try:
    print("passed here")
    # car_dict da speed key mavjud emas, shuning uchun AttributeError yuz beradi
    a = car_dict.speed
    result1 = car_dict["origin"]  # Toyota
    print(result1)
except AttributeError as err:
    print(f"Attribute error: {err}")
except KeyError as err:
    print(f"Key not found: {err}")
else:  # agar try blockida xatolik yuz bermasa, else bloki bajariladi
    print("No error occurred")
finally:  # har doim bajariladigan kod blokidir, xatolik yuz bermasa ham, yuz bersa ham bajariladi
    print("This block will always execute")
