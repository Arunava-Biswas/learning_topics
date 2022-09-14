# importing the modules
import os
from contextlib import contextmanager


# Here we will do the same task using a context manager
@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    except Exception as err:
        pass
    finally:
        os.chdir(cwd)


with change_dir('Sample-Dir-One'):
    print(os.listdir())

with change_dir('Sample-Dir-Two'):
    print(os.listdir())
