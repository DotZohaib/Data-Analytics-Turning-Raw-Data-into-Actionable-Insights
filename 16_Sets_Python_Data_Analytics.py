# A set is an unordered collection of unique elements.
# Sets are mutable, meaning you can add or remove elements after creation.
# Sets are useful for membership testing, removing duplicates from a sequence, and performing mathematical set operations
# like union, intersection, difference, and symmetric difference.

my_set = {1, 2, 3}
print(type(my_set))
print(my_set)

for i in my_set:
    print(i)
    
    
# Sets Functions and Methods

a = {1,2,3,4,5,6,7,8,9}

a.add(10) # Adding an element to the set
a.remove(5) # Removing an element from the set
a.pop() # Removing and returning an arbitrary element from the set
a.clear() # Removing all elements from the set
a.discard(5) # Removing an element from the set if it is a member. If the element is not a member, do nothing.
a.difference({1,2,3}) # Returning a new set with elements in the set that are not in the specified set
a.difference_update({1,2,3}) # Removing all elements of another set from
a.update([10,11,12,13,14,15]) # Updating a set with the union of itself and others
a.intersection({1,2,3,10,11}) # Returning a new set with elements common to the set and the specified set
a.intersection_update({1,2,3,10,11}) # Updating a set
a.copy() # Returning a shallow copy of the set
a.symmetric_difference({1,2,3,10,11}) # Returning a new set

print(a) # Printing the set after various operations



a = {1,2,3,4,5,6,7,8,9}
b = {5,6,7,8,9,10}

print(a.issubset(b)) # Checking if a set is a subset of another set
print(a.issuperset(b)) # Checking if a set is a superset of another set
print(a.isdisjoint(b)) # Checking if two sets have no elements in common
print(a.union(b)) # Returning a new set with elements from both sets
print(a.difference(b)) # Returning a new set with elements in the set that are not in the specified set
print(a.symmetric_difference(b)) # Returning a new set with elements in either the set or the specified set but not in both
print(a.intersection(b)) # Returning a new set with elements common to the set and the specified set