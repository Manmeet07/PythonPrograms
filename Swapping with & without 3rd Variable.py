print("USING THIRD VARIABLE")
num1=int(input("Enter first Number:"))
num2=int(input("Enter second Number:"))
Temp=num1
num1=num2
num2=Temp
print("Value of Num1 after swapping:",num1)
print("Value of Num2 after swapping:",num2)

print("WITHOUT USING THIRD VARIABLE")
num2,num1=num1,num2
print("Value of Num1 after swapping:",num2)
print("Value of Num2 after swapping:",num1)

print("USING PYTHON")
print("Value of Num1 after swapping:",num2)
print("Value of Num2 after swapping:",num1)
