# python has 7 types of operators
# 1. Arithmetic operators
a = 2 + 3
b = 3 - 1
c = 6 * 7
d = 8 / 2
print(a)
print(b)    
print(c)
print(d)
# 2. Assignment operators   
x = 5
x += 3  # x = x + 3
x = x * 2

print(x)
# 3. Comparison operators
y = 10
z = 20
print(y == z)  # Output: False
print(y > z)  # Output: False
print(y != z)  # Output: True
# 4. Logical operators
p = True
q = False
print(p and q)  # Output: False
print(p or q)  # Output: True
print(not(p or q))  # Output: True
# 5. Identity operators
m = ["apple", "banana"]
n = m
print(m is n)  # Output: True
print(m is not n)  # Output: False
# 6. Membership operators
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Output: True
print("grape" not in fruits)  # Output: True

# 7. Bitwise operators
a = 5  # 0101 in binary
b = 3  # 0011 in binary
print(a & b)  # Output: 0011 in binary, which is 3 in decimal
print(a | b)  # Output: 0111 in binary, which is 7 in decimal



