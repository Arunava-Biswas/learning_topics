# Decorators
# First check the First_Class_functions.py and closure.py files

"""
- A Decorator is a function that takes another function as argument, adds some kind of functionality and returns another function. All of these happen without altering the source code of the original function which has been passed in.
"""


# Example:
# Here the wrapper_function (inner function) will return a function that it accepts from the decorator_function (outer function) as an argument.
def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function


# Creating another function
def display():
    print("Run display function")


# Passing the display() as argument of the decorator_function() and storing it in a variable
decorated_display = decorator_function(display)
print("Here the decorated_display variable is equal to", decorated_display.__name__)
# Now running the wrapper_function with the help of the variable
# Here it executes the wrapper_function() which executes the original_function()
decorated_display()

print("\n")
print("\n")

"""
- Decorating a function allows us to easily add functionality to the existing functions, by adding that functionality inside a wrapper.
- So in the example without modifying the original display() we can go inside the wrapper_function() and execute any kind of code we want.
"""


def decorator_function(original_function):
    def wrapper_function():
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function


# Creating another function
def display():
    print("Run display function")


decorated_display = decorator_function(display)
decorated_display()

print("\n")
print("\n")


"""
- Now in python we use the '@' sign to define the decorator function like @decorator_function in top of the original function.
- This is the same thing as setting the original function equal to the function wrapped within the decorator.
"""


# Actual syntax used for decorator in python
def decorator_function(original_function):
    def wrapper_function():
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function


# Creating original function with decorator
@decorator_function
def display1():
    print("Run display function")


# Passing the display() to the decorator function
def display2():
    print("Run display function")


# Here it will print the same thing as previous case as we set up the 'display()' with the 'wrapper_function()' through the '@decorator_function'
display1()
# Doing the same explicitly
display2 = decorator_function(display2)
display2()
"""
So here declaring the decorator with the help of '@' is same as the display function is equal to decorator_function with the display function passed in to it as argument.
"""

print("\n")
print("\n")


"""
- The decorator function will not work if the original function took in any arguments. As here in case of the display_info() we passed 2 arguments but the original function in the decorator_function does not take any argument so if we use the @decorator_function with the display_info then it will throw error. 
"""


def decorator_function(original_function):
    def wrapper_function():
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function


@decorator_function
def display():
    print("Run display function")


@decorator_function
def display_info(name, age):
    print(f"Function display_info ran with arguments ({name}, {age})")


try:
    display_info("John", 25)    # Error is: wrapper_function() takes 0 positional arguments but 2 were given
except Exception as err:
    print("Error is:", err)


print("\n")
print("\n")

"""
- Now to be able to pass on any number of keyword argument to the wrapper and have it executed on our original function with those arguments we need to use the *args and **kwargs in the wrapper function.
- These will allow to accept any arbitrary number of positional or keyword arguments for the functions
"""


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):      # passing *args and **kwargs to the wrapper function
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)   # passing *args and **kwargs to the original function
    return wrapper_function


@decorator_function
def display():
    print("Run display function")


@decorator_function
def display_info(name, age):
    print(f"Function display_info ran with arguments ({name}, {age})")


# Now here the decorator function works with both the functions
try:
    display_info("John", 25)
    display()
except Exception as err:
    print("Error is:", err)


print("\n")
print("\n")

"""
- We can also use Classes as Decorators instead of using functions as Decorators.
"""


# Creating decorator class
class DecoratorClass(object):
    # passing the original_function into the class
    # Now the function is tied with any instance of this class
    def __init__(self, original_function):
        self.original_function = original_function

    # mimicking the wrapper_function() of the decorator function
    # for this we use the special method '__call__()'
    # Now everywhere we need to use the self.original_function as it is an instance
    def __call__(self, *args, **kwargs):
        print("call method executed this before {}".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


# Now using the DecoratorClass to decorate both the functions
@DecoratorClass
def display():
    print("Run display function")


@DecoratorClass
def display_info(name, age):
    print(f"Function display_info ran with arguments ({name}, {age})")


# Now here the decorator class works with both the functions
try:
    display_info("John", 25)
    display()
except Exception as err:
    print("Error is:", err)

