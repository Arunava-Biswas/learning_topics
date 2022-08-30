import datetime as dt


# Regular method of a class automatically takes the instance as the 1st argument, which by convention is called 'self'.
# Now to change a regular method to a classmethod we need to add a decorator called @classmethod at the top of the method.
# The @classmethod decorator basically altering the functionality of a method as now we will receive 'class' as the 1st argument automatically instead of the instance i.e. 'self', by convention it is called 'cls'.
# These class methods can also be used to provide multiple way of creating objects.
# The real life example of class method being used as constructor to create objects can be found in the 'datetime' module.
# In static method nothing is passed automatically as 1st argument. For static method we use decorator named @staticmethod.
# Here they pass neither the instance nor the class as the 1st argument, so they work just like a normal class.


class Employee:
    # class variables
    num_of_emp = 0
    raise_amt = 1.04

    # constructor
    # instance variables
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '_' + last + '@email.com'

        Employee.num_of_emp += 1

    # creating method for fullname
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # creating method for pay raise
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        return self.pay

    # now creating a class method
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # creating constructor using class method
    # here by convention the method name should have a 'from' to start with
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # using a static method to find whether a date is a workday or not?
    # here by convention the method name should start with 'is'
    @staticmethod
    def is_workday(day):
        # using python's inbuilt weekday method where 'Monday=0' and 'Sunday=6'
        if day.weekday() == 5 or day.weekday() == 6:
            return "is a holiday."
        else:
            return "is a workday."


# at the beginning number of employees
print('Number of employees at the beginning is:', Employee.num_of_emp)

# Creating objects
emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Arunava', 'Biswas', 60000)

print("\nAt the beginning the raise amount for the class and it's instances:")
print("Employee ->", Employee.raise_amt)
print("emp1 ->", emp1.raise_amt)
print("emp2 ->", emp2.raise_amt)

print('\nNow the full names of the employees:')
print(emp1.fullname())
print(emp2.fullname())
print('Number of employees now is:', Employee.num_of_emp)

print('\nNow the emails of the employees:')
print(emp1.fullname(), '->', emp1.email.lower())
print(emp2.fullname(), '->', emp2.email.lower())

print('\nInitial salaries of the employees:')
print(emp1.fullname(), '->', emp1.pay)
print(emp2.fullname(), '->', emp2.pay)

print('\nAfter raising salaries of the employees:')
print(emp1.fullname(), '->', emp1.apply_raise())
print(emp2.fullname(), '->', emp2.apply_raise())

print("\nNow after changing the raise amount for the Employee class using class method:")
# changing the class variable using the class method
Employee.set_raise_amt(1.05)
print("Employee ->", Employee.raise_amt)
print("emp1 ->", emp1.raise_amt)
print("emp2 ->", emp2.raise_amt)

print('\nAfter changing the raise amount of the employees using class method:')
print(emp1.fullname(), '->', emp1.apply_raise())
print(emp2.fullname(), '->', emp2.apply_raise())

# Now using class method creating new employees
# Here the data about employees are passed as string separated by '-'.
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# Now splitting the string to create a new employee
first_n, last_n, payment = emp_str_1.split('-')

# creating object
new_emp_1 = Employee(first_n, last_n, payment)

print("\nEmployee from string without class method:")
print(new_emp_1.fullname())
print(new_emp_1.fullname(), '->', new_emp_1.email.lower())
print(new_emp_1.fullname(), '->', new_emp_1.pay)

# The problem here is that everytime someone has to create a new employee they have to parse the values separately, so now let's create a constructor that will automatically do the task for them, for this we will use a class method.

# Now using the class method 'from_string()' let's create object employees
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print("\nEmployee from string using class method as constructor:")
print(new_emp_2.fullname())
print(new_emp_3.fullname())
print(new_emp_2.fullname(), '->', new_emp_2.email.lower())
print(new_emp_3.fullname(), '->', new_emp_3.email.lower())
print(new_emp_2.fullname(), '->', new_emp_2.pay)
print(new_emp_3.fullname(), '->', new_emp_3.pay)
print('Number of employees at the end is:', Employee.num_of_emp)

print('\nNow for the Static Method:')
# Here we will pass a date to the class Employee and use a static method to find out whether that date is a working day or not.
# For doing this we use the datetime module

# creating a date
my_date1 = dt.date(2022, 7, 24)     # it is a Sunday
my_date2 = dt.date(2022, 7, 29)     # it is a Friday
print(f"The day {my_date1} {Employee.is_workday(my_date1)}")
print(f"The day {my_date2} {Employee.is_workday(my_date2)}")

