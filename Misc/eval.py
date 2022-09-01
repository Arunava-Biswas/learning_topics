# Python Eval Function--Evaluating Expressions Dynamically

# syntax : eval("expression", global=None, local=None)

'''
How does Eval work:

1. Parse python Expression
2. Compile into a byte code
3. Evaluate the python expression
4. It will return the result
'''


'''
#Eval function evaluates python expressions which are written as strings
print(eval("5*5+7/2"))      # here 5*5+7/2 is written as string but the eval() is making the calculation out of a string.
print("\n")


# for e.g. if we enter expression sum([1,2,3,4,5]) we will get 15 as result
var1 = eval(input("Enter the python expression: "))
print(type(var1))
print(var1)                 # here it will show the result for the expression we have entered
print("\n")
'''


'''
# function for getting square of a number
def square_num(num):
    return num**2

print(square_num(3))
print(eval("square_num(3)"))   # using with eval()
print("\n")

# Always remember to keep the expression as string inside the eval()
'''


# this is for compile()
var = compile("5*5","<string>","eval")

print(eval(var))
print("\n")



### GLobals
# The Globals must be a dictionary and locals can be any mapping
x=10
result = eval("x+50+x**2",{"x":x})       # here x is specified as a global

print(result)                           # returns 160
print("\n")


# another example
x=100
z=100
result = eval("x+z+w",{"x":x,"z":100,"w":1000}) # here x,y,z are defined as global along with their values in dictionary form

print(result)                           # returns 1200
print("\n")



# Now for local
# here we will keep the 2nd value i.e. for global as empty and putting the dictionary in the local
result = eval("a+b+c",{},{"a":100,"b":200,"c":1000})

print(result)                           # returns 1200
print("\n")


# boolean expression
a=100
b=200
print(eval("a<b"))
print("\n")


# But also remember the eval() is insecure as it allows to execute dynamically arbitary code in python.