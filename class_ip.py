'''class deep diving
    (1) Encapsulation
    (2) Inheritance
    (3) Polymorphism
    (4) Abstraction
 '''
from unicodedata import name


print("=======Inheritance========")
# Parentn >> Child
# super() >> access parent class properties and methods

# ota class faqat ozining public va protected method va state larini child classga meros qilib beradi,
# lekin private method va state larni bermaydi


class Animal():
    # state
    description = "This is an animal class"
    # constructor

    def __init__(self, voice):
        self.voice = voice  # instance property
        self.status = "alive"  # instance property
    # method

    def make_sound(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):  # child class
    # constructor
    def __init__(self, sound, name, voice):
        # parent class constructor parent childga meros olish u-n majburiyat qoyadi
        super().__init__(voice)
        self.name = name
        self.sound = sound
# bu majburiyat esa shu voice ni qiymatni yuborishi kk bu "super()" degani parentdagi "__init__" methodni
# chaqirish va shu methodga argument berish degani va shu methodni chaqirish bn parentdagi "voice" ni qiymatini olish mumkin

    # method
    def introduce(self):
        print(
            f"Hi, my name is {self.name} and I am a dog and I can make sound: {self.sound}")

    def protect_owner(self):
        print(f"{self.name} is protecting his owner")


class Cat(Animal):  # child class
    # constructor
    def __init__(self, name, sound, color, voice):
        # bu child classda voice ni self.voice deb saqlaganimiz yoqmi chunki bu ishni alaqachin parent classda qilganmiz
        super().__init__(voice)
        # va shu parent classdagi voice ni child classda ham ishlatish mumkin, bu esa meros olishning bir qismi hisoblanadi
        self.name = name
        self.color = color
        self.sound = sound

    # method
    def introduce(self):
        print(
            f"Hi, my name is {self.name} and I am a cat and I can make sound: {self.sound} and my color is {self.color} i can make voice: {self.voice}")

    def catch_mouse(self):
        print(f"{self.name} is catching a mouse")


class Fish(Animal):  # child class
    # constructor
    def __init__(self,  name, voice, type):
        super().__init__(voice)
        self.name = name
        self.type = type

    # method
    def introduce(self):
        print(
            f"Hi, my name is {self.name} and I am a fish and I can make sound: {self.voice} and my type is {self.type}")

    def swim(self):
        print(f"{self.name} is swimming")


dog = Dog("Woof", "Rex", True)
cat = Cat("Mia", "Miew", "Black", True)
fish = Fish("Bubbles", False, "Goldfish")

dog.introduce()
dog.protect_owner()
cat.introduce()
cat.catch_mouse()
fish.introduce()
fish.swim()

print("=============")
dog.make_sound()  # parent method
cat.make_sound()  # parent method
fish.make_sound()  # parent method

print("=========")
print(Animal.description)  # parent property
# parent property bunda ota classdagi stateni child classda ham ishlatish mumkin
print(dog.description)

print(dog.voice, "\n", cat.voice, "\n", fish.voice)  # parent property
print(dog.status, "\n", cat.status, "\n", fish.status)  # parent property
