'''Tuples
    (1) What is Tuple: tuple vs list
    (2) Unpacking arguments
    (3) zip'''

print("=======What is Tuple: tuple vs list========")
# Tuple >> tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.
# List >> list is a collection which is ordered and changeable. Lists are written with square brackets.
#  Java/PHP/Nodejs array >> Python list

# literal
numbs = [1, 2, 3, 4, 5]

# constructor
# bunda string ichidagi har bir harf listning itemi sifatida olinadi yani ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd'] chiqadi
numbs2 = list("Hello World")
print(numbs)
print(numbs2)

fruits = ["apple", "banana", "cherry"]
print(fruits)
# bunda fruits listining 0-indexidagi item "orange" ga o'zgartiriladi yani ["orange", "banana", "cherry"] chiqadi
fruits[0] = "orange"
print(fruits)

# tuple
animals = ("cat", "dog", "rabbit")
tuple_obj = ("MIT", 100, True, None)
print(animals[0])
# bunda animals tuple ning 0-indexidagi item "lion" ga o'zgartiriladi
# animals[0] = "lion"
# yani TypeError: 'tuple' object does not support item assignment chiqadi
# print(animals)

#  try to avoid these
people = "Alice", "Bob", "Charlie"
animals = "cat",

print("=======Unpacking arguments========")
#  pythonda args ni yoyishni tuplelar orqali amalga oshiriladi
groups = ["MIT", "Harvard", "Stanford", "Yale", "Princeton", "Columbia"]
# bunda groups listining itemlari a, b, c ga tenglashtiriladi yani a=MIT, b=Harvard, c=Stanford chiqadi
(a, b, *c) = groups
print(f"a: {a}, b: {b}, c: {c}")

# *args === tuple


def calculate(*args):
    print("*args:", args)
    total = 1
    for num in args:
        total *= num
    print(f"the type of args: {type(args)} and the total: {total}")
    return total


calculate(2, 3, 4)
print("-"*10)
calculate(5, 6)

# **kwargs === dict


def introduce(**kwargs):
    print("**kwargs:", kwargs)
    print(
        f"Hi, my name is {kwargs.get('name')}, I am {kwargs.get('age')} years old and I live in {kwargs.get('city')}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print(f"the type of kwargs: {type(kwargs)}")


introduce(name="Alice", age=30, city="New York")
introduce(name="Bob", age=25, city="Los Angeles",
          profession="Developer", single=True)
