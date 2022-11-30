# Closures:
# First check the First_Class_functions.py file
"""
A Closure is a record storing a function together with an environment: a mapping associating each free variable of the function with the value or storage location to which the name was bound when the closure was created. A Closure, unlike a plain function, allows the function to access those captured variables through the Closure's reference to them, even when the function is invoked outside their scope.
"""


# Defining the functions
def outer_func1():
    message = "Hi"

    def inner_func1():
        print(message)

    return inner_func1()


# Calling the function
print("Executing and returning the inner function through the outer function")
outer_func1()

print("\n")


# Let's return the inner function without returning it.
# For that we remove the () of the inner function while returning it.

# Defining the functions
def outer_func2():
    message = "Hi"

    def inner_func2():
        print(message)

    return inner_func2


# Calling the function
print("Executing the inner function without returning through the outer function")
my_func = outer_func2()
print(my_func)      # It returns <function outer_func2.<locals>.inner_func2 at 0x00000221F5C92A60>
print("The name of the function attached to my_func is:", my_func.__name__)

print("\n")
print("Executing the variable a few times in a row")
my_func()
my_func()
my_func()
my_func()

# So a closure is an inner function that remembers and has access to variables to the local scope in which it was created even after the outer function has finished execution.

print("\n")


# Let's adding some parameters
def outer_func3(msg):
    message = msg                   # This is a free variable

    def inner_func3():
        print(message)

    return inner_func3


# Calling the function
print("Executing and returning the inner function with parameters passed through the outer function")
hi_func = outer_func3("Hi!")
hello_func = outer_func3("Hello!")

# Here each of the functions will remember the value of their own msg variable
hi_func()
hello_func()


