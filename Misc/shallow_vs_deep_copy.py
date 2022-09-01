# shallow copy vs deep copy

# remember whenever we need to apply shallow copy or deep copy the data that to be use should be collection because they are mutable.

lst1 = [1, 2, 3, 4]
lst2 = lst1

print(lst1)             # [1, 2, 3, 4]
print(lst2)             # [1, 2, 3, 4]
print("\n")

# now if we update an element in lst2 same will be reflected in lst1 also as both the variables here refering the same memory location.

lst2[1] = 1000

print(lst2)             # [1, 1000, 3, 4]
print(lst1)             # [1, 1000, 3, 4]
print("\n")


# now shallow copy
# here we will use .copy()

lst1 = [1, 2, 3, 4]
lst2 = lst1.copy()

# now again here we update an element of lst2 but here it will not be reflected in lst1 as here lst2 is a copy of lst1 and both have their separate memory locations.

lst2[1] = 2000

print(lst2)             # [1, 2000, 3, 4]
print(lst1)             # [1, 2, 3, 4]
print("\n")


# now if we create a nested list then this shallow copy definition gets changed a little bit.

# now shallow copy with nested list

lst1 = [[1, 2, 3, 4], [5, 6, 7, 8]]
lst2 = lst1.copy()


print(lst1)             # [[1, 2, 3, 4], [5, 6, 7, 8]]
print(lst2)             # [[1, 2, 3, 4], [5, 6, 7, 8]]
print("\n")

# difference from previous case is that there 1,2,3,4 were different elements of that list (1 dimensional) but here [1,2,3,4] as a total a single element in this nested list (2 dimensional).
# in a nested list these elements are considered as collection of items containing various objects. i.e. [1,2,3,4] is a collection of item and '1' is an object of that collection.
# now here if we change an element in lst1 that will get reflected in lst2 again because here both the variables are referring to the same object inside the nested list.

lst1[1][0] = 100

print(lst1)             # [[1, 2, 3, 4], [100, 6, 7, 8]]
print(lst2)             # [[1, 2, 3, 4], [100, 6, 7, 8]]
print("\n")

# now if we append to one of the lists because we have used shallow copy it will not get reflected to the other list.
# so here the new item we appended will not get copied but if we make some changes on the object that present inside the list that gets updated to the other list as well.

lst1.append([2, 3, 4, 5])

print(lst1)             # [[1, 2, 3, 4], [100, 6, 7, 8], [2,3,4,5]]
print(lst2)             # [[1, 2, 3, 4], [100, 6, 7, 8]]
print("\n")






# now deep copy
# for this we need to import copy and use .deepcopy()

import copy

lst1=[1,2,3,4]
lst2= copy.deepcopy(lst1)

print(lst1)             # [1, 2, 3, 4]
print(lst2)             # [1, 2, 3, 4]
print("\n")

# now here if we change one element in any list it will not gets reflected to the other one.
# so here it works as same like shallow copy when the list is 1 dimensional.

lst2[1] = 3000

print(lst2)             # [1, 3000, 3, 4]
print(lst1)             # [1, 2, 3, 4]
print("\n")



# but in case of nested list

lst1 = [[1,2,3], [3,4,5], [5,6,7]]
lst2 = copy.deepcopy(lst1)

print(lst1)             # [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
print(lst2)             # [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
print("\n")


# now if we change one element then it will not gets reflected to the other one as here again in deep copy a separate memory location gets created for everything we do in nested list.

lst2[1][0] = 200

print(lst2)             # [[1, 2, 3], [200, 4, 5], [5, 6, 7]]
print(lst1)             # [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
print("\n")


# Summarization
'''
in normal list(one Dm) : shallow copy == deep copy (as changes will take place to the other list also)
in nested list(multi Dm) : shallow copy != deep copy (as changes only in shallow copy gets reflected to other list)
'''