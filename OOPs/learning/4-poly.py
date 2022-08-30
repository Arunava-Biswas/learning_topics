# in-built polymorphic functions

# len() being used for a string
print(len("arunava"))

# len() being used for a list
print(len([10, 20, 30]))
print("\n")


# Polymorphism with class methods
# creating 1st class
class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


# creating 2nd class
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


# instantiation
obj_ind = India()
obj_usa = USA()

# for loop to call methods from each class
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()

print("\n")


# Method Overriding
class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")


class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


# instantiation
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()
obj_spr.intro()
obj_spr.flight()
obj_ost.intro()
obj_ost.flight()
print("\n")


# Implementing Polymorphism with a Function
"""
- Let's create a Function called 'func()' that will take an object as argument.
- Now let the function to do something with the object passed to it.
- Here we will call the methods which are defined in each of the two classes.
- Then instantiate both the classes and call their action using the same 'func()' function.
"""


# creating class 1
class India():
    # creating the methods
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


# creating class 2
class USA():
    # creating same methods in class 2 also
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


# creating the function to call the methods of the objects
def func(obj):
    obj.capital()
    obj.language()
    obj.type()


# instantiation
obj_ind = India()
obj_usa = USA()

# calling the function using the objects
func(obj_ind)
func(obj_usa)