# Importing module
from contextlib import contextmanager


# Decorator function
@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    except Exception as err:
        pass
    finally:
        f.close()


# Calling the generator function of the context manager
with open_file('sample2.txt', 'w') as f:
    f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

print(f.closed)
