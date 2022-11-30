# First-Class Functions:
# A programming language said to have First-Class Functions if it treats functions as First-Class citizens.

"""
First Class Citizen (Programming):
- A First-Class citizen (sometimes called First-Class Objects) in a programming language is an entity which supports all the operations generally available to other entities. These operations typically include being passed as an argument, returned from a function, and assigned to a variable.


Higher Order Functions:
- When a function accepts other functions as arguments or returns functions as their results then that function is called a Higher Order Function.
"""


# Creating a function
def square(x):
    return x * x


# Assigning the function to a variable
f1 = square(5)
# We can also assign the function to a variable without using the ()
# Remember keeping the () means calling/executing the function but here we are only assigning the function
f2 = square

# Now printing both the function and the variable
print("Assigning functions to a Variable:")
print(square)        # it will return <function square at 0x000001ADEDC6D1F0>
print(f2)            # it will return <function square at 0x0000014EB59AD1F0>
print(f1)            # it will return 25
print(f2(5))         # it will return 25

print("\n")
print("\n")


# Now let's pass functions as argument and return functions as result of other functions
# Passing a function as an argument: Example is the map()

# Creating a custom function
def cube(x):
    return x * x * x


# Defining our own map function
def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


# Calling the function 'my_map' to pass another function 'cube' and a set of array.
# The passed function will work on each element of the array and return the result.
cubes = my_map(cube, [1, 2, 3, 4, 5])
print("Passing function as an Argument:")
print(cubes)


print("\n")
print("\n")


# Now returning function as result of other function
def logger(msg):
    def log_message():
        print('Log:', msg)
    return log_message


print("Returning function as Result:")
# Here the log_hi variable is equal to log_message() as it is what has been returned by the logger()
log_hi = logger("Hi!")
# Now calling the log_message() using the variable log_hi
log_hi()

print("\n")
print("\n")


# Why returning a function as result from another function is important?

# Practical examples
def html_tag(tag):
    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag, msg))

    return wrap_text


# Here we are passing a tag and storing the function in a variable
print_h1 = html_tag('h1')
print(print_h1)             # It returns <function html_tag.<locals>.wrap_text at 0x000001EF6B2E2DC0>

# Now passing the message to the inner function with the help of the variable
print_h1('Test Headline')       # It returns <h1>Test Headline</h1>
print_h1('Another Headline')    # It returns <h1>Another Headline</h1>

print_p = html_tag('p')
print_p('Test Paragraph')


# This logic can be used for logging and in python we can also use it for decorating functions
