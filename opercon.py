'''OPERATORS AND CONDITIONS
    (1) Operators
    (2) Conditions
    (3) Logical Operators
'''

print("=======Operators========")
# Operators >> +, -, *, /, //, %, **, =, ==, !=, >, <, >=, <=
# Arithmetic Operators >> +, -, *, /, //, %, **
# Assignment Operators >> =, +=, -=, *=, /=, //=, %=, **=
# Comparison Operators >> ==, !=, >, <, >=, <=
# Logical Operators >> and, or, not
# Membership Operators >> in, not in
# Identity Operators >> is, is not

a = 19
b = 5

print(a / b)  # division operator
result = a // b  # floor division operator bunda bolingandagi butun qismi olinadi yani 3.8 emas 3 chiqadi
left = a % b  # modulus operator bunda bolingandagi qoldiq qismi olinadi yani 4 chiqadi
print(f"the result: {result} and the left: {left}")

# exponentiation operator bunda b ning 2-darajasi olinadi yani 25 chiqadi
print("b*b:", b**2)
# exponentiation operator bunda b ning 3-darajasi olinadi yani 125 chiqadi
print("b*b*b:", b**3)

print("="*10)  # bu pythonda ruxsat etilgan erkinlik yani shi "=" ni 10 marta takrorlashni anglatadi va natijada "==========" chiqadi


c = dict(name="Kevin", age=40)
d = dict(name="Kevin", age=40)
e = c

print(c == d)  # comparison operator bunda c va d ning qiymatlari tengmi yoki yoqmi tekshiriladi va natijada True chiqadi
#  pythonda faqat qiymatlar solishtiriladi lekin nodejsda kabi tillarda reference yani manzil solishtiriladi va natijada False chiqadi
# id() function bunda c va d ning manzillari olinadi va natijada har ikkisi uchun ham har xil manzil chiqadi
print(id(c), id(d), id(e))  # c va e ning manzillari bir xil

data = c is d  # identity operator bunda c va d ning manzillari tengmi yoki yoqmi tekshiriladi va natijada False chiqadi
print(data)
print(c is e)  # identity operator bunda c va e ning manzillari tengmi yoki yoqmi tekshiriladi va natijada True chiqadi


print("=======Conditions========")
# Conditions >> if, elif, else
# Conditionlar har doim "Tuethy" yoki "Falsy" qiymatlarni tekshiradi

x = 5

if x > 50:  # agar shu berilgan qiymat "Tuethy" bo'lsa, ya'ni bu shart bajarilsa, quyidagi kod bajariladi
    print("case A")
elif x > 10:
    print("case B")
else:
    print("case C")

print("=======Logical Operators========")
# Logical Operators >> and, or, not
# and operator bunda har ikkala shart ham "Tuethy" bo'lsa,
# or operator bunda har ikkala shartdan biri "Tuethy" bo'lsa,
# not operator bunda shart "Tuethy" bo'lsa "Falsy" ga, "Falsy" bo'lsa "Tuethy" ga aylanadi

age = 25
# person = None

# if age > 16:
#     person = "Adult"
# else:
#     person = "Child"

# print(f"Person is: {person}") # Adult

# Ternary bn yoki shartli operator bn yuqoridagi kodni qisqartirish mumkin
person = "Adult" if age > 16 else "Child"
print(f"Person is: {person}")  # Adult

print("="*10)

is_student = True
is_admin = False
is_guest = False
is_parent = True

if not is_student:
    print("Welcome, do you want to enroll in our courses?")
elif is_admin:
    print("Welcome, admin! You have full access to the system.")
elif is_guest or is_parent:
    print("Welcome, you may go to the waiting room.")
else:
    print("Others, welcome! Please wait for further instructions.")
