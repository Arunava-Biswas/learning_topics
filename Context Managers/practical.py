# Importing module
import os

#### CD Example ####
# without the context manager
# So here in the code we first go to the directory then we change directory then print all the files in that directory then again we change directory back to our original parent directory. And we do this multiple times.

cwd = os.getcwd()
os.chdir('Sample-Dir-One')
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir('Sample-Dir-Two')
print(os.listdir())
os.chdir(cwd)

# Running the code will result the following
'''
['mydoc.txt', 'todo.txt', 'work.txt']
['demo.txt', 'sample.txt', 'test.txt']
'''
