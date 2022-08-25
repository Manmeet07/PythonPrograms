A=int(input("Enter First Number : "))
B=int(input("Enter Second Number : "))
C=int(input("Enter Third Number : "))

if(A>B and A>C):
    print("Largest Number is : ",A)
elif (B>C):
    print("Largest Number is :" ,B)
else:
    print("Largest Number is :", C)
