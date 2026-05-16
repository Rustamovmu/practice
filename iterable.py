print("=======Iterable objects and range========")
# Iterable objects >> list, tuple, set, dict, string, zip, range, file, etc

text = "MIT"
for i in text:
    print(f"the letter is {i}")


range_obj = range(5)  # 0,1,2,3,4
print("Range object is ", range_obj)
for i in range_obj:
    print(f"the number is {i}")

print("=======Dictionaries========")
# Dictionaries >> key-value pairs
# dict is a built-in class in python
# Dictionaries are JSON object!
person = {
    "name": "Kevin",
    "age": 40,
    "city": "New York",
    "single": True
}
# kop hollarda dict() methodu ishlatiladi
person_object = dict(name="Kevin", age=40, city="New York", single=True)
print(f"Person dictionary is {person}")
print(f"Person object is {person_object}")

name = person["name"]
print(f"Name is {name}")

age = person_object["age"]
print(f"Age is {age}")

#  method get() >> agar key mavjud bo'lsa, qiymatni qaytaradi, aks holda None qaytaradi
city = person.get("city")
print(f"City is {city}")
country = person.get("country")
# agar key mavjud bo'lmasa, default qiymatni qaytaradi
balance = person.get("balance", 1000)
print(f"Country is {country}, Balance is {balance}")

del person["single"]  # single key-value juftini o'chiradi
for key in person:
    print(f"Key is {key}, Value is {person[key]}")

print("===============")

for key in person_object:
    print(f"Key is {key}, Value is {person_object.get(key)}")
