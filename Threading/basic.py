# Importing the library
import time

# Starting a counter, so we can measure how long the entire task took to complete
start = time.perf_counter()


# Creating a function that will print then sleep for 1 sec and then again print
def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')


# Calling the function multiple times
do_something()
do_something()
do_something()

# Getting the finish time
finish = time.perf_counter()

# Printing the total time taken
print(f"Task finished in {round(finish - start, 2)} second(s).")
