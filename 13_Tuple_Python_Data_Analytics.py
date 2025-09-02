# A tuple is an immutable sequence of values that can store multiple items .
# a tuple are ordered and allow duplicate values.
# Useful for storing fixed collections of items.

# my_tuple = (1, 2, 3,2,3,1,2,34,5,6,72,3,4,5,2) # parentheses are optional
my_tuple = 1, 2, 3,2,3,1,2,34,5,6,72,3,4,5,2 # parentheses are optional
b = "DotZohaib"  # this is string but if used comma then it is also a tuple
# b = ("DotZohaib",) # single element tuple, comma is necessary
print(my_tuple)
print(type(my_tuple))


#  slicing and Iteration in tuple 

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(a[2:5])
print(a[:5])
print(a[2:])
print(a[::2])



# Iteration in tuple in python for loop
for i in a:
    print(i)
    
# range in tuple
for i in range(len(a)):
    print(a[i])
    
    
# while loop in tuple
i = 0
while i <= len(a):
    print(a[i])
    i += 1
    
    

# conversion of tuple and tuple functions 

z = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Before conversion of tuple to list", type(z))

a = list(z)  # tuple to list conversion
print("After conversion of tuple to list", type(a))

a.append(10)  # now we can add element in list
print(a)

b = tuple(a)  # list to tuple conversion
print("After conversion of list to tuple", type(b))
print(b)
print(b.count(2))  # count function in tuple
print(b.index(5))  # index function in tuple