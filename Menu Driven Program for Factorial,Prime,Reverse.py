while True:
    print("1.Factorial")
    print("2.Prime")
    print("3.Reverse")
    break
ch=int(input("Enter your Choice:"))
if ch==1:
    num=int(input("Enter Number:"))
    fact=1
    for i in range(num):
        fact=fact*(i+1)
    print("Factorial of",num,":",fact)
elif ch==2:
    a=int(input("enter Number:"))
    k=0
    for i in range(2,a//2+1):
        if(a%i==0):
            k=k+1
            print("Number is prime")
        else:
            print("Number isn't Prime")
elif Ch==3:
    N=int(input("Enter Number:"))
    rev=0
    while(N>0):
        dig=N%10
        rev=rev*10+dig
        N=N//10
    print("Reverse of Number:",rev)
else:
    print("Invalid Option")
    
