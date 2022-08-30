class MyClass:
    # Hidden member of MyClass
    __hiddenVariable = 0

    # A member method that changes hiddenVariable
    def add(self, increment):
        self.__hiddenVariable += increment
        print(self.__hiddenVariable)


# Driver code
myObject = MyClass()
myObject.add(2)
myObject.add(5)

# Here it throws an exception when we try to access a hidden variable outside the class
try:
    print(myObject.__hiddenVariable)
except Exception as e:
    print("Error is: ", e)

print("\n")

# Now accessing the variable
myObject1 = MyClass()
print(myObject1._MyClass__hiddenVariable)
print("\n")


# Public, Private, Protected
class Courses:
    # Creating attributes
    course1 = "Data Science"        # public
    _course2 = "Web Development"    # protected
    __course3 = "Data Analytics"    # private


class Course1(Courses):
    def Coursename(self):
        print(f"The first course is: {Courses.course1}")


class Course2(Courses):
    def __init__(self):
        Courses.__init__(self)

    def Coursename1(self):
        print(f"The second course is: {self.course2}")

    # Accessing protected variable from a subclass
    def Coursename2(self):
        print(f"The second course is: {self._course2}")


class Course3(Courses):
    def __init__(self):
        Courses.__init__(self)

    def Coursename1(self):
        print(f"The third course is: {self.course3}")

    # Accessing private variable from outside the class of its own
    def Coursename2(self):
        print(f"The third course is: {self._Courses__course3}")


# Initializing
c1 = Course1()
c2 = Course2()
c3 = Course3()

# Accessing the public variable
print("The Public attribute of the parent class is: ", c1.course1)
print("The Public attribute of the child class 1 is: ", c2.course1)
print("The Public attribute of the child class 2 is: ", c3.course1)
print("\n")

# Accessing the protected variable
try:
    print(c2.Coursename1())     # this will throw an error as we try to call a protected attribute of the parent class
except Exception as e:
    print("Error is: ", e)

# Now printing the protected variable
c2.Coursename2()

# Accessing the private variable
try:
    print(c3.Coursename1())     # this will throw an error as we try to call a private attribute of the parent class
except Exception as e:
    print("Error is: ", e)

# Now printing the private variable
c3.Coursename2()

# So now directly printing all the members outside the class
print("\nPrinting all the members from outside of the parent class using a child class:")
print("The Public attribute is: ", c3.course1)
print("The Protected attribute is: ", c3._course2)
print("The Private attribute is: ", c3._Courses__course3)
print("\n")


# Even by an object of the main class we are not able to call the private variable outside the class
c0 = Courses()
try:
    print(c0.__course3)
except Exception as e:
    print("Error is: ", e)


print("Correct way to call the Private variable is: ", c0._Courses__course3)