# is vs ==


"""
'==' it is for comparison. But here both the elements we are comparing will have different memory locations.

'is' it is a keyword. Here it not only compare, but it also checks the memory location of the elements. Here only one object gets created and that will be referred by both the variables. Here if we make changes in the object through one variable then that change will take place on the other variable also as they are both sharing the same object.
"""

lst1 = ["Arun", "Arun1", "Arun2"]
lst2 = ["Arun", "Arun1", "Arun2"]

print(lst1 == lst2)            # here we are comparing both the lists on the basis of the elements inside them
print("\n")


print(lst1 is lst2)            # here it is false as both are different objects in different memory locations
print("\n")

# Now let's assign lst1 to lst3 and then see what will happen

lst3 = lst1

print(lst1 is lst3)         # here it is true as both are referring to same object
print("\n")

# make change in lst3

lst3[0] = "Jana"

print(lst3)
print(lst1)
print("\n")                # here change has taken place in both the variables
