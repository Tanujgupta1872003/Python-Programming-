# Calculate Simple Interest
p = float(input("Enter Value of Pricipal: "))
r = float(input("Enter Value of Rate of Intrest: "))
t = float(input("Enter Value of Time: "))

si = (p*r*t)/100
amt = p+si
print("Simple Interest  = ",si)
print("Amount is = ",amt)