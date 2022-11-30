# Decorators

# mainly used in flask and django


# function copy

def welcome():
    print("Welcome to learn advance python.")


welcome()

print("\n")


def greet():
    return "Welcome to learn advance python."


# now if we put this function into a variable and then print it then we will see the same message.
# now even if we delete the function the variable where we copied the function will still work properly. This is called function copy.

grt = greet()
del greet

print(grt)
print("\n")

# greet()     // now it will throw NameError: name 'greet' is not defined


# closure

# whenever we write function inside a function then it is called closure function.
# in closure, we are able to provide whatever input we want into the main function, and also we can define our inner function inside that specific function we can also use that particular variable that is available in the main function.

'''
def main_welcome(msg):
    # msg = "Hello Everyone"        // it will also work if it is put inside the function instead of a parameter
    def sub_welcome_class():
        print("Welcome to Python.")
        print(msg)                  # using the variable from the main_welcome function
        print("Please keep watching")
    return sub_welcome_class()


main_welcome("Hello Everyone")
'''

print("\n")

#  another closure with some changes. Here we are passing an inbuilt function "print" to the main function as a parameter and calling it from the sub function. Here the parameter for the func() is the message it prints.

'''
def main_welcome(func):

    def sub_welcome_class():
        print("Welcome to Python.")
        func("This is another way for closure.")                 
        print("Please keep watching")
    return sub_welcome_class()


main_welcome(print)
print("\n")
'''


# closures are initial decorators.


# decorators
# in decorators inside a function we can also give a function as parameter instead of a specific variable or a message.

def main_welcome(func):
    def sub_welcome_class():
        print("Welcome to Python.")
        print(func([1, 2, 3, 4, 5, 6]))  # now here it will print 6 as the length of the list
        print("Please keep watching")

    return sub_welcome_class()


main_welcome(len)
print("\n")

# now calling a self defined function channel_name() inside another function main_function.

'''
def main_function(func):      
    def sub_function():
        print("Welcome to Python.")
        func()              
        print("Please keep watching")
    return sub_function()


def channel_name():
    print("This is Krish Youtube channel.")


# now to call

main_function(channel_name)
print("\n")
'''


# The other way is to define a decorator using @functionName before the custom function to call the function.


def main_function(func):
    def sub_function():
        print("Welcome to Python.")
        func()
        print("Please keep watching")

    return sub_function()


@main_function  # this is defining the decorator and calling the function
def channel_name():
    print("This is Krish Youtube channel.")