# Positional argument: When we define a parameter in a function and call that function by providing specific value to the function, then it is called 'Positional Argument'.
# Keyword argument: When we set the parameter value while defining the function then it will be a 'Keyword argument'. If we want to change it back to a positional then just pass the value of the parameter.
# When we use '*args' means we are speaking about Positional Argument.
# When we use '**kwargs' means we are speaking about Keyword Argument.

# Positional argument
def hello1(name, age):
    print(f"Hello {name}, you are {age} years old.")


# Keyword argument
def hello2(name='Arun', age=32):
    print(f"Hello {name}, you are {age} years old.")


hello1("Arunava", 35)  # calling the function with positional argument
hello2()               # calling the function with keyword argument
hello2("Arunava", 35)  # changing back to a positional argument by passing the values

print("\n")


def hello(*args, **kwargs):
    print(args)             # it will return a tuple with positional arguments
    print(kwargs)           # it will return a dictionary with keyword arguments


hello('Arunava', 'Biswas', age=35, dob=1987)

# But there is a problem. Say if we create a list for the positional arguments and a dictionary for the keyword arguments and pass them to the function in that case it will take everything as a positional argument.

lst = list(('Arunava', 'Biswas'))
dict_val = {'age': 35, 'dob': 1987}

print("\nPassing them without specifying which one is positional and which one is keyword:")
hello(lst, dict_val)

# To overcome this problem use the '*' for the positional arguments and '**' for the keyword arguments

print("\nPassing them specifying which one is positional and which one is keyword using the '*'s:")
hello(*lst, **dict_val)