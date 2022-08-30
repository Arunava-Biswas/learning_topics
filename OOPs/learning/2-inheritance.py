# Inheritance

# parent class
class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display(self):
        print(self.name)
        print(self.id_number)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.id_number))


# child class
class Employee(Person):
    def __init__(self, name, id_number, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, id_number)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.id_number))
        print("Post: {}".format(self.post))


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
b = Person('John', 456765)

# calling a function of the class Person using its instance
a.display()
a.details()
print("\n")


# to check the subclass and instance
print(issubclass(Employee, Person))     # here it will be 'True' as 'Employee' is a subclass of 'Person'
print(issubclass(Person, Employee))     # here it will be 'False' as 'Person' is not a subclass of 'Employee'
print(isinstance(b, Employee))          # here it will return 'False' as 'b' is not an instance of 'Employee' class
print(isinstance(a, Person))          # here it will return 'True' as 'a' is an instance of 'Person' class
print("\n")


# the '__init__()' in inheritance
class A(object):
    def __init__(self, something):
        print("A init called")
        self.something = something


class B(A):
    def __init__(self, something):
        # Calling init of parent class
        A.__init__(self, something)
        print("B init called")
        self.something = something


obj1 = B("Something")
print("\n")

# So, the parent class constructor is called first. But in Python, it is not compulsory that the parent class constructor will always be called first. The order in which the __init__ method is called for a parent or a child class can be modified. This can simply be done by calling the parent class constructor after the body of the child class constructor.


class A(object):
    def __init__(self, something):
        print("A init called")
        self.something = something


class B(A):
    def __init__(self, something):
        print("B init called")
        self.something = something
        # Calling init of parent class
        A.__init__(self, something)


obj2 = B("Something")
print("\n")


# accessing parent members in a subclass:

# Using parent class name
class Base(object):
    # Constructor
    def __init__(self, x):
        self.x = x


class Derived(Base):
    # Constructor
    def __init__(self, x, y):
        Base.x = x                  # using the parent class name to access
        self.y = y

    def printXY(self):
        # print(self.x, self.y) will also work
        print(Base.x, self.y)


# Driver Code
d = Derived(10, 20)
d.printXY()
print("\n")


# Using the super()
class Base(object):
    # Constructor
    def __init__(self, x):
        self.x = x


# In Python 3.x, "super().__init__(name)" also works
class Derived(Base):
    # Constructor
    def __init__(self, x, y):
        super(Derived, self).__init__(x)        # using super()
        self.y = y

    def printXY(self):
        # here we don't need the 'Base.x' because super() is used in constructor
        print(self.x, self.y)


# Driver Code
d = Derived(10, 20)
d.printXY()
