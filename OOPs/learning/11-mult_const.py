# To initialize multiple constructor we need to initialize the constructor with '*args'. The '*args' is the positional argument. We can also initialize multiple constructors in a class using a keyword argument i.e. '**kwargs'. Now by creating if else condition we can create multiple objects of different size constructors. But it is not a good practice

class Animal1:
    # 1st constructor with 2 attributes
    def __init__(self, name, species):
        self.name = name
        self. species = species

    # 2nd constructor with 3 attributes
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    # creating a method
    def make_sound(self, sound):
        return "The animal is {} and it says {}.".format(self.name, sound)

    def __repr__(self):
        return "Animal('{}', '{}', '{}')".format(self.name, self.species, self.age)


# Initializing
print("Creating an object using 2 attributes (Using constructor 1):")
try:
    dog = Animal1("Dog", "mammals")
    print(dog)
    print(dog.make_sound("bhow bhow"))
except Exception as err:
    print('Error is: ', err)

# Here it will throw an error: Error is:  __init__() missing 1 required positional argument: 'age'
print("\nCreating an object using 3 attributes (Using constructor 2):")

try:
    dog = Animal1("Dog", "mammals", 9)
    print(dog)
    print(dog.make_sound("bhow bhow"))
except Exception as err:
    print('Error is: ', err)

print("\nUsing a hack to create multiple constructors:")


class Animal2:
    # creating constructor with *args
    def __init__(self, *args):
        if len(args) == 1:          # if only one argument is passed then create just one attribute
            self.name = args[0]
        elif len(args) == 2:        # if two arguments is passed then create just two attributes
            self.name = args[0]
            self.species = args[1]
        elif len(args) == 3:        # if three arguments is passed then create just three attributes
            self.name = args[0]
            self.species = args[1]
            self.age = args[2]

    # creating a method
    def make_sound(self, sound):
        return "The animal is {} and it says {}.".format(self.name, sound)


# Initializing
print("\nCreating different objects of different size attributes:")
try:
    dog = Animal2("Dog")
    cat = Animal2("Cat", "mammals")
    snake = Animal2("Snake", "reptile", 5)
    print("\nObject1")
    print(dog.name)
    print(dog.make_sound("bhow bhow"))

    print("\nObject2")
    print(cat.name)
    print(cat.species)
    print(cat.make_sound("meow meow"))

    print("\nObject3")
    print(snake.name)
    print(snake.species)
    print(snake.age)
    print(snake.make_sound("hiss hiss"))
except Exception as err:
    print('Error is: ', err)
