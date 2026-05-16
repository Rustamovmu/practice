'''Lists
(1) working with lists
(2) list methods
(3) Lambda function
(4) enumerate, map, filter
'''

print("=======Working with lists========")
# Java/PHP/Nodejs array >> Python list
# List >> list is a collection which is ordered and changeable. Lists are written with square brackets.


# list literal
person = {"name": "Alice", "age": 30, "city": "New York"}  # dict literal
people = ("Bob", "Charlie", "David")  # tuple literal
groups = ["MIT", "Harvard", "Stanford"]  # list literal
for university in groups:
    print(f"the university is {university}")


#  constructor
# bunda string ichidagi har bir harf listning itemi sifatida olinadi yani ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd'] chiqadi
letters = list("Hello World")
print(
    f"the letters list is {letters} and length of the list is {len(letters)}")

print("-"*10)
fruits = ["apple", "banana", "cherry"]
# bunda fruits listining 0-indexidagi item "apple" ga tenglashtiriladi yani a=apple chiqadi
a = fruits[0]
# bunda fruits listining -1-indexidagi item "cherry" ga tenglashtiriladi yani b=cherry chiqadi
b = fruits[-1]
# bunda fruits listining 1-indexidan boshlab 3-indexigacha itemlar "banana" va "cherry" ga
c = fruits[1:3]
# tenglashtiriladi yani c=['banana', 'cherry'] chiqadi
# bunda fruits listining 0-indexidan boshlab 2 qadam bilan itemlar "apple" va "cherry" ga
d = fruits[::2]
# tenglashtiriladi yani d=['apple', 'cherry'] chiqadi
# bunda fruits listining itemlari teskari tartibda olinadi yani e=['cherry', 'banana', 'apple'] chiqadi
e = fruits[::-1]
print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}")

print("===== List methods ========")
# List methods >> append(),  insert(), remove(), pop(), clear(), index(), sort(), reverse()

letters = ["H", "e", "l", "o"]

letters.append("c")  # add behind
print(f"the appended letters list is {letters}")
print("-"*10)

letters.insert(1, "a")  # add in the middle
print(f"the inserted letters list is {letters}")
print("-"*10)

letters.remove("l")  # remove by value
print(f"the removed letters list is {letters}")
print("-"*10)

size = len(letters) - 1
result1 = letters.pop(size)  # remove by index
print(
    f"the popped letters list  is {letters} and the removed item is {result1}")
print("-"*10)

result2 = letters.pop(0)  # remove the first item
print(
    f"the popped letters list  is {letters} and the removed item is {result2}")
print("-"*10)

letters.clear()  # clear the list
print(f"the cleared letters list is {letters}")

print("-"*10)
animal = ["cat", "dog", "rabbit", "capybara", "hamster"]
print(f"the animal list is {animal}")

animal.remove("capybara")  # remove by value
print(f"the removed animal list is {animal}")

del animal[2:4]  # remove by index
print(f"the deleted animal list is {animal}")

exist = animal.index("dog")  # index of the item
print(f"the index of the item is {exist}")

# animal.clear()  # clear the list
# print(f"the cleared animal list is {animal}")

if "cat" in animal:  # check if the item exists in the list
    print("the item exists in the list")
else:
    print("the item does not exist in the list")

print("-"*10)
numbers = [5, 2, 9, 1, 5, 6]
print(f"the numbers list is {numbers}")
numbers.sort()  # sort the list in ascending order
print(f"the sorted numbers list is {numbers}")
numbers.sort(reverse=True)  # sort the list in descending order
print(f"the sorted numbers list in reverse is {numbers}")
print("-"*10)

# immutable >> sorted() index() method
# function bunda numbers listining sortlangan yangi versiyasi olinadi yani [1, 2, 5, 5, 6, 9] chiqadi
# lekin numbers listi o'zgarmaydi yani [5, 2, 9, 1, 5, 6] chiqadi
numbers2 = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers2)  # sort the list in ascending order
print(f"the sorted numbers list is {sorted_numbers}")
print(f"the original numbers list is {numbers2}")

print("=======Lambda function========")
# Lambda function >> lambda arguments: expression
# Lambda function is a small anonymous function that can take any number of arguments,
# but can only have one expression. Lambda functions are often used as a shortcut for defining simple functions.


def calculate(x, y): return x * y


result = calculate(5, 3)
print(f"the result of the calculate function is {result}")

print("-"*10)
# Lambda function
people = [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 35)
]
people.sort()
print(f"the sorted people list is {people}")
print("-"*10)

#  sorted by age via lambda function
# sort the list of dictionaries by age
people.sort(key=lambda person: person[1])
print(f"the sorted people list is {people}")
