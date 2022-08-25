L=[]
N=int(input("Enter No. of Elements u want to add : "))
for c in range(N):
    Num=int(input("Enter Data Element : "))
    L.append(Num)
print(L)

Num2=int(input("Enter Number to be search : "))
f=0
for x in L:
    if (x==Num2):
        f=1
        print("Search Found ")
        break
if (f==0):
    print("Search Not found ")
