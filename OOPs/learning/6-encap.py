# Creating a Base class
class Base:
    def __init__(self):
        self.a = "Arunava Biswas"
        self.__c = "Arunava Biswas"


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)

try:
    print(obj1.c)
except Exception as e:
    print("Error is: ", e)


try:
    obj2 = Derived()
except Exception as e:
    print("Error is: ", e)
print("\n")


# base class
class iNeuron:
    def __init__(self):
        self.course1 = "Data Science"   # public variable
        self.__course2 = "Big Data"     # private variable

    def students(self):
        print("The students are from the course: ", self.course1)

    def students1(self):
        print("The students are from the course: ", self.__course2)

    # Creating a method to change the value of the private attribute
    def students_change(self, new_value):
        self.__course2 = new_value     # changing the value of the private variable


# creating objects
i1 = iNeuron()
i2 = iNeuron()

# Here it will print the default value Data Science
i1.students()

# Now changing the value of the attribute course1
i1.course1 = "Data Analytics"
# Now the value will change to Data Analytics
i1.students()

# So basically here we are able to override the value of the public variable in the runtime.

# Now try to do the same as above i.e. override the value but this time for the private variable.

# Here it will print the default value of Big Data
i2.students1()

# Now changing the value of the attribute __course2
i2.__course2 = "Blockchain"

# Here it will not change the value of the private attribute and return the default value
i2.students1()

# Now call the method to reassign the value
i2.students_change("Blockchain")

# Here the value will change to Blockchain
i2.students1()

