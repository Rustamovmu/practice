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
