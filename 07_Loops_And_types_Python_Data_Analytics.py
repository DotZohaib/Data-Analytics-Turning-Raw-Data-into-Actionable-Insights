#  Introduction to loops and types in Python for Data Analytics
# how mani types of loof are there in python

# 1. for loop
# 2. while loop

for i in range( 2, 21, 2):
   print(i)


# while loop

i = 2
while i <= 20:
    # print(i)
    i = i + 2  # valid in python
    # i++  # not valid in python
    # i += 2 # valid in python


x = int(input("Enter the starting number: "))
z = int(input("Enter the number to print the table: "))
while x <=10:
    print(f"{z} x {x} = {z*x}")
    x += 1


while True:
    print("Hello World")
    # break  # to stop the infinite loop
    # continue  # to skip the current iteration and continue with the next iteration
    # pass  # to do nothing and continue with the next iteration


while True:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the Second number: "))

    print("Total numbers between", a, "and", b, "are:", a + b)

    exit = input("Do you want to exit? (yes/NO)")
    if (exit == "yes") or (exit == "YES"):
        break


#nested loop
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
    
    
# for loop conditional statement 

for i in range(1, 6):
    if i == 3:
        print("This is three")
    print(i)
    
# break and continue in for loop
for i in range(1, 6):
    if i == 3:
        break
    print(i)
for i in range(1, 6):
    if i == 3:
        continue
    print(i)