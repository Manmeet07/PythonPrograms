#1 Recursively find the factorial of a natural number.
Num=int(input("Enter a Number:"))
Factorial=1
for i in range(Num):
    Factorial=Factorial*(i+1)
print('Factorial of',Num,'=',Factorial)
       
