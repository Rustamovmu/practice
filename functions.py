'''FUNCTIONS
(1) DEFINE vs CALL
(2) Paramets and Arguments
(3) Keyword and default arguments
(4) Scope
'''

# bu builtins dunder olinmoqda built in function
print("======== DEFINE and CALL =========")

# build in functions => print() type() .....
# Function - reusable block of code
# in JAVA we use {} for block, but in Python it has indentation concept

# DEFINE - parameter
# def greet(a):
#     pass  #DEFINE qilib hech bir ish bajarmasa function indentationnidan chiqish uchun pass syntaxni yozish kerak


def greet(a):
    print(f"How do you do, {a}")


# CALL - argument
greet("Kevin")

res1 = greet("MIT42")
print("In Python output of VOID Functions is ", res1)
# REATURN and VOID
# VOID function output is None


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


res2 = greeting("Fede")
print("Return Function output used with return syntax:", res2)


print("======== Keyword and default arguments =========")


# def give(name, age):
#     print("give is executed")
#     return f"{name} is {age} yeard old"

def give(name, age=25):
    print("give is executed")
    return f"{name} is {age} yeard old"


res3 = give(name="Kevin", age=40)
print(res3)

res4 = give(name="Fede")
print(res4)


print("======== SCOPE =========")
'''
Priority 
(1) Determines inside function
(2) Determines in paramentes and arguments
(3) Determines outside of function
'''

b = 100


def calc(a, b):
    c = a * b
    print(f"{c}")


calc(10, 10)


def calc2(a):
    c = a * b
    print(f"{c}")


calc2(10)
