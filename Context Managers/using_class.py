# Creating a class
class Open_File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    # to set up the context manager
    # here we will open the file
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    # to tear down the context manager
    # the file gets closed automatically
    # the parameters are therefore if we throw an exception, and we can use these to access that information
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


# Now using the context manager
with Open_File('sample1.txt', 'w') as f:
    f.write('Testing')

# To check that the file is closed outside the context manager
print(f.closed)     # it will return 'TRUE' outside the context manager, that the file is in fact closed
