bs = float(input("Enter basic Salary: "))

hr = (12.5/100)*bs
da = (7.5/100)*bs
tax = (2.5/100)*bs

netsal = bs + hr + da -tax

print("House Rent = ",hr)
print("Daily Allowances = ",da)
print("Tax = ",tax)
print("Net Salary = ",netsal)
