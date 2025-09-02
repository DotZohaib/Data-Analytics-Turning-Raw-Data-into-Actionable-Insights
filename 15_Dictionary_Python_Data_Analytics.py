# A dictionary is an unordered collection of key-value pairs, where each key is unique.
# Dictionaries are used to store and manage data in a structured way.
# Dictionaries are mutable, which means you can change the elements of a dictionary after it has been created.

my_dict = {'name': 'iqra', 'age': 20, 'city': 'karachi'}
print(type(my_dict))
print(my_dict['name'])
print(my_dict['age'])
print(my_dict['city'])


# Iteration in dictionary

stu = {'name': 'iqra', 'age': 20, 'city': 'karachi'}

for i in stu:
    print(i)  # it will print only keys

for i in stu.values():
    print(i)  # it will print only values

for i in stu.items():
    print(i)
    
    
    
# Dictionary Functions
stu = {'name': 'iqra', 'age': 20, 'city': 'karachi'}

#Get method
print(stu.get('name'))  # it will print value of name key
print(stu.get('country', 'Not Found'))  # if key is not found then it will print Not Found

# keys() method
print(stu.keys())  # it will print all keys in dictionary

# values() method
print(stu.values())  # it will print all values in dictionary

# items() method
print(stu.items())  # it will print all items in dictionary

# update() method
stu.update({'age': 21})  # it will update the value of age key
print(stu)

# copy() method
new_stu = stu.copy()  # it will create a copy of the dictionary
print(new_stu)



# Iteration in dictionary

stu = {'name': 'iqra', 'age': 20, 'city': 'karachi'}

# setdefault() method
print(stu.setdefault('name', 'Not Found'))  # it will print value of name key

# pop() method
print(stu.pop('age'))  # it will remove the age key and return its value
print(stu)

# popitem() method
print(stu.popitem())  # it will remove the last inserted key-value pair and return

# clear() method
stu.clear()  # it will remove all items from the dictionary
print(stu)
# del keyword
del stu  # it will delete the dictionary
print(stu)  # it will raise an error because the dictionary is deleted
# Note: Be careful while using del keyword because it will delete the dictionary permanently.


# Dictionary Nested 

my_dict = {'name': 'iqra', 'age': 20, 'city': 'karachi', 'marks': {'math': 90, 'science': 80}}
print(my_dict)
print(my_dict[1]["math"])