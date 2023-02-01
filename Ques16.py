a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

if a>b:
    for i in range(a-1,b,-1):
        if i%2==0:
            print(i)
else:
    for i in range(b-1,a,-1):
        if i%2==0:
            print(i)
