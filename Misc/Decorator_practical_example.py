import time
from functools import wraps


# Practical example of decorator.
# One of the most common cases for decorator in python is logging.
# Another example is to use the timing function to see how much time a function takes to run
# Here we want to keep track of how many times a specific function runs and what arguments are passed to that function
# In Wrapper function:
# Here it logs the function and also logs the arguments in that function
# Then we run the original function with the arguments and keywords and return the result
# Lastly we are returning the wrapper function that allows us to run all of these with the added functionality
# We can see the log results in files named display_info.log for display_info() and when run with both the decorators commenting out the individual ones we will get result in wrapper.log for display_info()
# Here when we ran both the decorators at same time then at first the @my_timer decorator runs with the orig_function, and it returns the wrapper. Then this wrapper get passed to the @my_logger decorator as original function, that is why we get a new log file as here the argument passed in the orig_func of my_logger() is different that when we used only the @my_logger decorator independently.
# So you see if we change the order of the decorators there can be very unusual results.

# It is best practice to save the information of our original function whenever we use decorators.
# To do this we need to use the 'functools' module and the 'wraps' decorator.
# Here we use a decorator inside a decorator.
# All we have to do is decorate all of our decorators inside the 'wraps' decorator.
# So we need to add the '@wraps()' at every wrapper function and pass the original function as argument to it.
# After doing this now even if we run both decorators we will get the result in display_info.log file as now each decorator will return the original function and not the wrapper as in the earlier case.


# This is the decorator function with the original function as argument
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    # This is the wrapper function that takes the arguments and keywords arguments as parameters
    # To save the original information
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args: {args}, and kwargs: {kwargs}")
        return orig_func(*args, **kwargs)

    return wrapper


# Using with the timer
# Here the logic is same as logging
def my_timer(orig_func):
    import time

    # To save the original information
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{orig_func.__name__} function ran in : {t2} secs.")
        return result

    return wrapper


'''
@my_logger
def display_info(name, age):
    print(f"Function display_info ran with arguments ({name}, {age})")


@my_timer
def display(name, age):
    time.sleep(1)  # so the program take 1 sec to execute
    print(f"Function display ran with arguments ({name}, {age})")
'''


# applying both the decorators on one function
# Here it is the stacked version it is similar to:
# display_info = my_logger(my_timer(display_info))
# So here the lower decorator in the stack gets executed before the higher one
'''
@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)  # so the program take 1 sec to execute
    print(f"Function display ran with arguments ({name}, {age})")
'''


# After using the @wraps(orig_func)
# Now the order does not matter
@my_timer
@my_logger
def display_info(name, age):
    time.sleep(1)  # so the program take 1 sec to execute
    print(f"Function display ran with arguments ({name}, {age})")


# using with logging
'''
try:
    print("\nRuns with logging decorator")
    display_info("Robert", 38)
except Exception as err:
    print("Error is:", err)


# using with timer
try:
    print("\nRuns with timer decorator")
    display("Michael", 35)
except Exception as err:
    print("Error is:", err)
'''

# using with both
try:
    print("\nRuns with both decorators")
    display_info("Nathan", 43)
except Exception as err:
    print("Error is:", err)
