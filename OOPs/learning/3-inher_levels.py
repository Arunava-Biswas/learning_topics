# Single Inheritance:
# Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code re-usability and the addition of new features to existing code.

# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")


# Derived class
class Child(Parent):
    def func2(self):
        print("This function is in child class.")


# Driver's code
obj = Child()
obj.func1()
obj.func2()
print("\n")


# Multiple Inheritance:
# When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. In multiple inheritances, all the features of the base classes are inherited into the derived class.

# Base class1
class Mother:
    mother_name = ""

    def mother(self):
        print(self.mother_name)


# Base class2
class Father:
    father_name = ""

    def father(self):
        print(self.father_name)


# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.father_name)
        print("Mother :", self.mother_name)


# Driver's code
s1 = Son()
s1.father_name = "RAM"
s1.mother_name = "SITA"
s1.parents()
print("\n")


# Multilevel Inheritance :
# In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. This is similar to a relationship representing a child and a grandfather.

# Base class
class Grandfather:
    def __init__(self, grandfather_name):
        self.grandfather_name = grandfather_name


# Intermediate class
class Father(Grandfather):
    def __init__(self, father_name, grandfather_name):
        self.father_name = father_name
        # invoking constructor of Grandfather class using the parent class name
        Grandfather.__init__(self, grandfather_name)


# Derived class
class Son(Father):
    def __init__(self, son_name, father_name, grandfather_name):
        self.son_name = son_name
        # invoking constructor of Father class
        Father.__init__(self, father_name, grandfather_name)

    def print_name(self):
        print('Grandfather name :', self.grandfather_name)
        print("Father name :", self.father_name)
        print("Son name :", self.son_name)


# Driver code
s1 = Son('Prince', 'Rampaul', 'Lal mani')
print(s1.grandfather_name)
s1.print_name()
print("\n")


# Hierarchical Inheritance:
# When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance. In this program, we have a parent (base) class and two child (derived) classes.

# Base class
class Parent:
    def func1(self):
        print("This is a function call from parent class.")


# Derived class 1
class Child1(Parent):
    def func2(self):
        print("This is a function call from child1 class.")


# Derived class 2
class Child2(Parent):
    def func3(self):
        print("This is a function call from child2 class.")


# Driver's code
obj1 = Child1()
obj2 = Child2()
obj1.func1()
obj1.func2()
obj2.func1()
obj2.func3()
print("\n")


# Hybrid Inheritance:
# Inheritance consisting of multiple types of inheritance is called hybrid inheritance.

class School:
    def func1(self):
        print("This function is in school.")


class Student1(School):
    def func2(self):
        print("This function is in student 1. ")


class Student2(School):
    def func3(self):
        print("This function is in student 2.")


class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")


# Driver's code
obj3 = Student3()
obj3.func1()
obj3.func2()
obj3.func4()