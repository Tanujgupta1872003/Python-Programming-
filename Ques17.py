n = int(input("Enter Number: "))
f = 0
for i in range(1,n+1):
    if n%i==0:
        f+=1
if f==2:
    print("Prime Number")
else:
    print("Not a Prime Number")
