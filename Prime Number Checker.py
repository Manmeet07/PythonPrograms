a=int(input("Enter Number:"))
k=0
for i in range(2,a//2+1):
    if(a%i==0):
        k=k+1
if(k<=0):
    print("Number is Prime")
else:
    print("Number isn't Prime")
    
