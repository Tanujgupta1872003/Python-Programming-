f1 = int(input("Enter Height 1 in Feets: "))
f2 = int(input("Enter Height 2 in Feets: "))
i1 = int(input("Enter Height 2 in Inches: "))
i2 = int(input("Enter Height 2 in Inches: "))

f3 =  (f1+f2) + (i1+i2) // 12
i3 = (i1+i2)%12

print("Total Feets = ",f3)
print("Total Inches = ",i3)
