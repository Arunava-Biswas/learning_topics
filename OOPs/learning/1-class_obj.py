# Creating a class
class Animal:
    # Constructor method
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def Dog_behaviour(self):
        print(f"{self.name} is a {self.breed} dog and it is {self.age} years old.")


# Creating object of the class
dog = Animal('Tommy', 'GSD', 5)
dog.Dog_behaviour()
print("\n")

# Here the identity can be considered as the name of the dog
# State of attributes are the breed, age etc.
# Behaviour is whether the dog is eating or sleeping.


# A Sample class with __init__ method
class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)


# Creating different objects
p1 = Person('Nikhil')
p2 = Person('Abhinav')
p3 = Person('Anshul')

p1.say_hi()
p2.say_hi()
p3.say_hi()
print("\n")

# Here a person named 'Nikhil' is created. While creating a person, “Nikhil” is passed as an argument, this argument will be passed to the __init__ method to initialize the object. The keyword self represents the instance of a class and binds the attributes with the given arguments.


# Class attribute and instance attribute
class Dog:
    # class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name


# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))
print("\n")


# Creating class and objects with methods
class Dog:
    # class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name

    # class method
    def speak(self):
        print("My name is {}".format(self.name))


# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class methods
Rodger.speak()
Tommy.speak()
