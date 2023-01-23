q1=int(input("Enter sales made in quarter 1: "))
q2=int(input("Enter sales made in quarter 2: "))
q3=int(input("Enter sales made in quarter 3: "))
q4=int(input("Enter sales made in quarter 4: "))
total = q1+q2+q3+q4
comm = total*(3.5/100)
print("Total sales made in a year = ",total)
print("Commission earned = ",comm)
