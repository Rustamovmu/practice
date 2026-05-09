print("====== NUMBERS ======")

# in Java, variable is name of storage location!
# in Python, variable is named reference!

count = 100
count_type = type(count)
print("count:", count, count_type)

print(f"the count: {count} and type: {count_type}")

result1 = count.bit_count()  # method

result2 = count.numerator  # state
print(result1, result2)


print("====== STRING ======")

# METHODS: upper() lower() title() find() replace()


course = "AI Python FULLstack"

result = type(course)
print(f"the type pf course: {result}")

result = course.title()
print(f"the result 1: {result}")

result = course.upper()
print(f"the result 2: {result}")

result = course.replace("FULLstack", "MasterClass")

print(f"the result 4: {result}")


print("====== BOOLEAN ======")

# functions => type() input() bool() int() str()

# y = input("Give value: ")

# print("y:", y)

# result = y.isnumeric()

# print(f"the input value is numeric: {result}")


# TRUTHY vs FALSY value

# TRUTHY ==> True  100  -100 "MIT"
# FALSY ==> False 0 "" None

test_falsy = ""
print("The FALSY 1 :", bool(test_falsy))

test_falsy = "" or False or None or 0
print("The FALSY 2:", bool(test_falsy))

test_falsy = "" or False or None or 0 or 100
print("The FALSY 3 :", bool(test_falsy))

test_falsy = "" and False and None and 100
print("The FALSY 3:", bool(test_falsy))


test_truthy = "MIT42"
print("The TRUTHY:", bool(test_truthy))
