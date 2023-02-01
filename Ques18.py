mk={}
for i in range(1,6):
    k=int(input("Enter marks: "))
    mk[i]=k
print(mk)
s=0
av=0
for i in mk:
    print(i,"Roll no having ",mk[i]," marks")
    s=s+mk[i]
print("Total marks of the class = ",s)
av=s/len(mk)
print("Average marks = ",av)
