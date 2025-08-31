# sum of even number 1 to 50 

sum = 0
for i in range (2, 52, 2):
    sum += i
print("Sum of even numbers from 1 to 50 is:", sum)

# print square of first 20 numbers

for j in range(1, 21):
    print(j , j**2)


# find the sum of old 10 numbers 

summ = 0 
for z in range(1,10, 2):
    summ += z
print(summ)



while True:
    name = input("Enter your name: ")
    total = 0
    
    while True:
        print("Enter the amount and quantity")
        amount = int(input("Enter the amount: "))
        quantity = int(input("Enter the quantity: "))
        total += amount * quantity
        print("Total amount: ", total)
        
        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != "yes":
            break

    print("Total amount for", name, "is:", total)


for i in range (1, 10):
    for j in range(1, i +1):
        print(j, end=" ")
    print()
    
for i in range (1, 10):
    for j in range(1, i +1):
        print("*", end=" ")
    print()
    
for i in range (1, 10):
    for j in range(1, i +1):
        print(i, end=" ")
    print()
    
for i in range (1, 10):
    for j in range(6, i,-1):
        print(j, end=" ")
    print()