# Importing the library
import concurrent.futures
import time

# Starting a counter, so we can measure how long the entire task took to complete
start = time.perf_counter()


# Creating a function that will print then sleep for user defined seconds and then again print
def do_something(seconds):
    print(f'Sleeping {seconds} seconds...')
    time.sleep(seconds)
    return f'\nDone Sleeping...{seconds}'


# Creating context manager
'''
# This is for the single time by using submit()
with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 1)
    print(f1.result())
    print(f2.result())
'''

# This is for multiple times in a loop using list comprehension
with concurrent.futures.ThreadPoolExecutor() as executor:
    # creating a list for seconds to sleep
    secs = [5, 4, 3, 2, 1]
    # results = [executor.submit(do_something, 1) for _ in range(10)]
    # results = [executor.submit(do_something, sec) for sec in secs]

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    # using a map()
    # here the results would return in order they have started
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

finish = time.perf_counter()

# Printing the total time taken
print(f"Task finished in {round(finish - start, 2)} second(s).")
