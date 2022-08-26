Num1=int(input("Enter a 3-Digit Number:"))
f=Num1
sum=0
while(f>0):
    a=f%10
    f=int(f/10)
    sum=sum+(a**3)
if(sum==Num1):
    print("Armstrong Number of",Num1,":",sum)
else:
    print(Num1,"Doesn't have armstrong Number")
    
