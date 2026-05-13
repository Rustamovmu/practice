''' Class deep diving
    (1) Encapsulation
    (2) Inheritance
    (3) Polymorphism
    (4) Abstraction
 '''

print("=======Encapsulation========")
# Encapsulation >> public, __private, _protected


class Account():
    # state
    description = "This is an account class"
    # constructor

    def __init__(self, owner, amount):
        self.__owner = owner  # public property
        self.__amount = amount  # private property
    # methods

    def get_balance(self):
        # public method
        print(f"the owner {self.__owner} has ${self.__amount}")

    def deposit(self, amount):
        print("desposit method called")
        self.__amount += amount  # private method

    def withdraw(self, amount):
        print("withdraw method called")
        if amount <= self.__amount:
            self.__amount -= amount  # private method
        else:
            print("Insufficient funds")

    @property
    def holder(self):
        return self.__owner
# bu bn shu ownerni qiymatini tashqaridan olish mumkin, lekin o'zgartirish mumkin emas,
#  bu encapsulationning bir qismi hisoblanadi va buni method dek emas balki state sifatida ishlatish mumkin
# buni shu holatida "getter" deyiladi va bu bn maxfiy malumotlarni tashqaridan olish mumkin

    @holder.setter
    def holder(self, new_owner):
        print("holder setter called", new_owner)
        self.__owner = new_owner
# bu bn shu ownerni qiymatini tashqaridan o'zgartirish mumkin, va pastdagi holatda method qilib chaqirish kk edi bu bn esa
#  state qilib ishlatish mumkin

    def change_owner(self, new_owner):
        print("change_owner method called", new_owner)
        # public method. bu oddiy method bn ownerni ozgartirish lekin buni boshqa yaxshiroq yoli ham bor
        self.__owner = new_owner


account1 = Account("Kevin", 1000)
account1.get_balance()  # public method

print("-------")
account1.deposit(3500)  # public method
account1.withdraw(2000)  # public method
account1.get_balance()  # public method

print("-------")
# print(account1.owner)
try:
    result = account1.__amount  # private property
    print(result)
except Exception as err:
    print("Error:", err)

# public property bu yerda buni state sifatida ishlatish mumkin, method emas
account_owner = account1.holder
print(account_owner)  # Kevin deb chiqarib berdi pasda

# Kevin deb chiqarib berdi pasda
# Kevin deb chiqarib berdi pasda
print("owner before change:", account1.holder)
account1.change_owner("Fede")  # public method
print("owner after change:", account1.holder)  # Fede deb chiqarib berdi

# public method buni shunchaki "Alice" ga tenglab olib ishlatilyapdi tepadagi dek qiyin emas
account1.holder = "Alice"
print("owner after change with setter:", account1.holder)  # Alice deb chiqarib
