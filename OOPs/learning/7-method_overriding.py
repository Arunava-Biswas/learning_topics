class ineuron:
    def student(self):
        print("print the details of all the students")


class ineuron_vision(ineuron):
    # override the method inherited from the parent class
    def student(self):
        print("these are the filters student list ")


# instantiation
stu1 = ineuron()
stu2 = ineuron_vision()

stu1.student()      # this will call the method in the parent class
stu2.student()      # this will call the redefined method in the child class
print("\n")


# Method overriding with multiple inheritance

# Defining parent class 1
class Parent1:
    # Parent's show method
    def show(self):
        print("Inside Parent1")


# Defining Parent class 2
class Parent2:
    # Parent's show method
    def display(self):
        print("Inside Parent2")


# Defining child class
class Child(Parent1, Parent2):
    # Child's show method
    def show(self):
        print("Inside Child")


# Driver's code
obj = Child()

obj.show()          # it will show the value of the child class due to method overriding
obj.display()       # it will show the default value
print("\n")


# Method overriding with multilevel inheritance

# parent class
class Parent:
    # Parent's show method
    def display(self):
        print("Inside Parent")


# Inherited or Sub class (Note Parent in bracket)
class Child(Parent):
    # Child's show method
    def show(self):
        print("Inside Child")


# Inherited or Sub class (Note Child in bracket)
class GrandChild(Child):
    # Child's show method
    def show(self):
        print("Inside GrandChild")


# Driver code
g = GrandChild()
g.show()            # here it will override the show() of the child class
g.display()         # this will remain same as in the parent class
print("\n")


# Calling the Parent’s method within the overridden method

# Using Classname
class Parent:

    def show(self):
        print("Inside Parent")


class Child(Parent):

    def show(self):
        # Calling the parent's class method
        Parent.show(self)
        print("Inside Child")


# Driver's code
obj = Child()
obj.show()
print("\n")


# using super()
class Parent:

    def show(self):
        print("Inside Parent")


class Child(Parent):

    def show(self):
        # Calling the parent's class method
        super().show()
        print("Inside Child")


# Driver's code
obj = Child()
obj.show()
