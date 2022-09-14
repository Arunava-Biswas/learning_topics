# Importing the library
import threading
import time

# Starting a counter, so we can measure how long the entire task took to complete
start = time.perf_counter()

'''
# Creating a function that will print then sleep for 1 sec and then again print
def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('\nDone Sleeping...')
'''


# Creating a function that will print then sleep for user defined seconds and then again print
def do_something(seconds):
    print(f'Sleeping {seconds} seconds...')
    time.sleep(seconds)
    print('\nDone Sleeping...')


'''
# Creating threads manually
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)
t3 = threading.Thread(target=do_something)


# Running the threads
t1.start()
t2.start()
t3.start()


# Using join method
t1.join()
t2.join()
t3.join()
'''

# Creating a list of threads
threads = []

# Now creating multiple (10) threads using a loop
for _ in range(10):
    # t = threading.Thread(target=do_something)
    t = threading.Thread(target=do_something, args=[1.5])       # passing argument to the function
    t.start()
    threads.append(t)

# Now using the join on all the threads
for thread in threads:
    thread.join()

# Getting the finish time
finish = time.perf_counter()

# Printing the total time taken
print(f"Task finished in {round(finish - start, 2)} second(s).")
