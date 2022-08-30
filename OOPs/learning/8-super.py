class Emp:
    def __init__(self, id, name, Add):
        self.id = id
        self.name = name
        self.Add = Add


# Class freelancer inherits EMP
class Freelance(Emp):
    def __init__(self, id, name, Add, Emails):
        super().__init__(id, name, Add)
        self.Emails = Emails


Emp_1 = Freelance(103, "Suraj kr gupta", "Noida", "KKK@gmails")
print('The ID is:', Emp_1.id)
print('The Name is:', Emp_1.name)
print('The Address is:', Emp_1.Add)
print('The Emails is:', Emp_1.Emails)
print("\n")


# Super function in single inheritance
class Animals:
    # Initializing constructor
    def __init__(self):
        self.legs = 4
        self.domestic = True
        self.tail = True
        self.mammals = True

    def isMammal(self):
        if self.mammals:
            print("It is a mammal.")

    def isDomestic(self):
        if self.domestic:
            print("It is a domestic animal.")


class Dogs(Animals):
    def __init__(self):
        super().__init__()

    def isMammal(self):
        super().isMammal()


class Horses(Animals):
    def __init__(self):
        super().__init__()

    def hasTailandLegs(self):
        if self.tail and self.legs == 4:
            print("Has legs and tail")


# Driver code
Tom = Dogs()
Bruno = Horses()

Tom.isMammal()
Bruno.hasTailandLegs()
print("\n")


# Super function in multiple inheritances
class Mammal:
    def __init__(self, name):
        print(name, "Is a mammal")


class canFly(Mammal):
    def __init__(self, canFly_name):
        print(canFly_name, "cannot fly")

        # Calling Parent class
        # Constructor
        super().__init__(canFly_name)


class canSwim(Mammal):
    def __init__(self, canSwim_name):
        print(canSwim_name, "cannot swim")

        super().__init__(canSwim_name)


class Animal(canFly, canSwim):
    def __init__(self, name):
        # Calling the constructor of both the parent class in the order of their inheritance
        super().__init__(name)


# Driver Code
Carol = Animal("Dog")


# Super function in Multi-Level inheritance
class Mammal:
    def __init__(self, name):
        print(name, "Is a mammal")


class canFly(Mammal):
    def __init__(self, canFly_name):
        print(canFly_name, "cannot fly")

        # Calling Parent class Constructor
        super().__init__(canFly_name)


class canSwim(canFly):

    def __init__(self, canSwim_name):
        print(canSwim_name, "cannot swim")
        super().__init__(canSwim_name)


class Animal(canSwim):
    def __init__(self, name):
        # Calling the constructor of both the parent class in the order of their inheritance
        super().__init__(name)


# Driver Code
Carol = Animal("Dog")
print("\n")


# Program to define the use of super() function in multiple inheritance
class GFG1:
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG1)')

    def sub_GFG(self, b):
        print('Printing from class GFG1:', b)

    # class GFG2 inherits the GFG1


class GFG2(GFG1):
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG2)')
        super().__init__()

    def sub_GFG(self, b):
        print('Printing from class GFG2:', b)
        super().sub_GFG(b + 1)

    # class GFG3 inherits the GFG1 ang GFG2 both


class GFG3(GFG2):
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG3)')
        super().__init__()

    def sub_GFG(self, b):
        print('Printing from class GFG3:', b)
        super().sub_GFG(b + 1)


# main function
if __name__ == '__main__':
    # created the object gfg
    gfg = GFG3()

    # calling the function sub_GFG3() from class GHG3 which inherits both GFG1 and GFG2 classes
    gfg.sub_GFG(10)