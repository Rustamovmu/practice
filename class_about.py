'''CLASS
    (1) what is a class?
    (2) oridinary vs static properties and methods
    (3) special methods
'''

print("=======what is a class?========")
# class >> blueprint for creating objects
# stucture >> state constructors, methods


class Person():
    # state
    message = "class state property"

    # constructor
    def __init__(self, name, age):
        self.name = name  # instance property
        self.age = age  # instance property

    # method
    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old")

    def say_age(self):
        print(f"hi, my name is {self.name} and I am {self.age} years old")

    @classmethod
    def class_method(cls):
        print("This is a class method")


person1 = Person("Kevin", 40)
person2 = Person("Fede", 30)
person3 = Person("Alice", 25)

#  ordinary state
print(person1.name)  # instance property

# ordinary method
person1.introduce()  # instance method
person2.say_age()  # instance method

print("=======oridinary vs static properties and methods========")
# static state
new_message = Person.message  # class property
print(new_message)

# static method
Person.class_method()  # class method

print("=======special methods========")
# special methods >> __init__, __str__, __len__, __new__, __getitem__, __eq__, etc


class Car():
    #  state
    description = "This is a car class"
    # constructor

    def __new__(cls, *args, **kwargs):
        print("**__new__ method is called**")
        return super().__new__(cls)

    def __init__(self, model, year):
        self.model = model
        self.year = year
    # method

    def start_engine(self):
        print(f"{self.model} engine started")

    def stop_engine(self):
        print(f"{self.model} engine stopped")

    def __str__(self):
        return f"{self.model} is produced in ({self.year})"

    def __call__(self):
        print(f"{self.model} is called as a function")
        return True


my_car = Car("Toyota Camry", 2020)
my_car.start_engine()
my_car.stop_engine()


print("============")
your_car = Car("Honda Accord", 2019)
print(your_car)
your_car()
result = your_car()
print(f"Result of calling your_car as a function is {result}")
