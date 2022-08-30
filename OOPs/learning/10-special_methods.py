# __repr__() : It makes an unambiguous representation of the object, and should be used for debugging, logging etc. It is mainly used for other developers to read the code. Good practice to write this method is to try to display something that can be copied and paste back to the python code that will recreate the same object.
# __str__() : It is more readable representation of the object so the end user can make sense of its code.
# The str method gets preference over the repr method if both gets called.

class Employee:
    # class variables
    raise_amt = 1.04

    # constructor
    # instance variables
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '_' + last + '@email.com'

    # creating method for fullname
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # creating method for pay raise
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        return self.pay

    # repr method
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    # str method
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # creating a special customized add method to calculate total salary by passing employees
    # it takes 2 parameters:
    # 'self' it stays left side of the addition
    # 'other' it stays right side of the addition
    def __add__(self, other):
        return self.pay + other.pay

    # dunder len method to get fullname
    def __len__(self):
        return len(self.fullname())


# Creating objects
emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Arunava', 'Biswas', 60000)

# without __repr__()
# print(emp1)             # it returns: <__main__.Employee object at 0x00000207C61D9FD0>

# Now after __repr__()
print(emp1)               # it returns: Employee('Corey', 'Schafer', '50000')

# Now we can create another object with the output we get from repr().

print(emp2)              # it returns: Arunava Biswas - Arunava_Biswas@email.com

# Now printing both the methods
print(repr(emp1))
print(str(emp2))
print("\n")


# There are other special methods also:
# Like in integer there is __add__() and also in string there is another __add__()
# These methods used to work in the background
print(2 + 5)
print(int.__add__(2, 5))        # using __add__()
print(str.__add__('Arunava ', 'Biswas'))
print("\n")

# We can make customization with this dunder methods
# Let's say we want to calculate total salary just by adding the employees of the Employee class together.
print('Combined salary of the employees are:')
print(emp1 + emp2)

# the len() is also a special method
# Let's use the __len__() to get the length of the employee full name.
print("\nThe length of fullname of the employees are:")
print(f"Length of {emp1.fullname()} is {len(emp1)}")
print(f"Length of {emp2.fullname()} is {len(emp2)}")