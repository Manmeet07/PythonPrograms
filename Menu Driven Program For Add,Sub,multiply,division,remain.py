while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Floor Division")
    print("6.Remainder")
    break
ch=int(input("Enter Your Choice;Enter 0 to Exit:"))
if ch==1:
    Num1=int(input("Enter First Number:"))
    Num2=int(input("Enter Second Number:"))
    Sum=Num1+Num2
    print("Sum:",Sum)
if ch==2:
    Num1=int(input("Enter First Number:"))
    Num2=int(input("Enter Second Number:"))
    Diff=Num1-Num2
    if Num2>Num1:
     Diff=Num2-Num1
    print("Difference:",Diff)
elif ch==3:
   Num1=int(input("Enter First Number:"))
   Num2=int(input("Enter Second Number:"))
   Multi=Num1*Num2
   print("Product:",Multi)
elif ch==4:
    Num1=int(input("Enter First Number:"))
    Num2=int(input("Enter Second Number:"))
    Div=Num1/Num2
    if Num2>Num1:
       Div=Num2/Num1
       print("Division:",Div)
elif ch==5:
    Num1=int(input("Enter First Number:"))
    Num2=int(input("Enter Second Number:"))
    flor_Div=Num1//Num2
    if Num2>Num1:
       Flor_Div=Num2//Num1
       print("Floor Division:",Flor_Div)
elif ch==6:
    Num1=int(input("Enter First Number:"))
    Num2=int(input("Enter Second Number:"))
    Rem=Num1%Num2
    if Num2>Num1:
       Rem=Num2%Num1
       print("Remainder:",Rem)
elif ch==0:
    exit
else:
    print("Invalid Option")
    
    
    
    
