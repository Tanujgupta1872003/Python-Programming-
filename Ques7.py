m1 = int(input("Enter Initial Reading of Meter: "))
m2 = int(input("Enter Final Reading of Meter: "))
rate = int(input("Enter Rate per Unit: "))
part = int(input("Number of Consumers: "))

units = m2-m1
Bill = rate*units
Div_Bill = Bill/part

print("Total Units Consumed = ",units)
print("Electicity Bill = ",Bill)
print("Each Has to pay = ",Div_Bill)
