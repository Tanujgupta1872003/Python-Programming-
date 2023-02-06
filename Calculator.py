print("Select Operator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Floor Division")

n1 = float(input("Enter First Number: "))
n2 = float(input("Enter Second Number: "))

choice = int(input("Enter Your Choice: "))
if choice == 1:
    sum = n1 + n2
    print("Answer = ",sum)
elif choice == 2:
    sum = n1-n2
    print("Answer = ",sum)
elif choice == 3:
    sum = n1*n2
    print("Answer = ",sum)
elif choice == 4:
    sum = n1/n2
    print("Answer = ",sum)
elif choice == 5:
    sum = n1%n2
    print("Answer = ",sum)
elif choice == 6:
    sum = n1//n2
    print("Answer = ",sum)
else:
    print("Invalid Input")
