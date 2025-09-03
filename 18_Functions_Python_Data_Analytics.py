# A function is a block of reusable code that performs a specific task.
# Functions help in organizing code, improving readability, and avoiding redundancy.
# In Python, functions are defined using the 'def' keyword followed by the function name and


# function is two types  1) Defined the function  2) Call the function                   #  parentheses. Functions can take parameters (inputs) and can return values (outputs).


# def my_function(a , b):
#     # print(a * b)
#     return a * b

# print(my_function(5, 10))




def hello(name):
    print("Hello How are you " + name + " ?")
    
hello("Zohaib")
# hello("Ali")



# return statement and Recursion  in function

def value():
    return 10
print(value())


def fack(n):
    if n == 0:
        return 1
    else:
        return n * fack(n - 1)
print(fack(5))