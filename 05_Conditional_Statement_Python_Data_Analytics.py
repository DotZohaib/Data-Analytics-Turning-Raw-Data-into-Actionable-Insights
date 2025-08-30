Marks = 5

if Marks >= 80:
    print("Grade A")
    if Marks >= 90:
        print("You are eligible for scholarship")
elif Marks >= 60:
    if (Marks >= 70):
        print("You are eligible for sports quota")
    print("Grade B")
elif Marks >= 40:
    if (Marks >= 50):
        print("You are eligible for extra classes")
    print("Grade C")
else:
    print("Fail")
    if (Marks < 20):
        print("You are not eligible for re-exam")