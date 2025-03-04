a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
choice = int(input("What do you want to do:\n1. Add \n2. Subtract \n3.Multiply \n4. Divide"))
if choice == 1:
    res = a+b
elif choice == 2:
    res = a-b
elif choice == 3:
    res = a*b
else:
    res= a//b
print(f"The result is {res}")
