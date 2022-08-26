Amount=float(input("Enter the Principle Amount:"))
Time=int(input("Enter the time in Years:"))
Rate=float(input("Enter the Rate:"))
Simple_interest=(Amount*Time*Rate)/100
print("The simple Interest is",Simple_interest)
Compound_interest=Amount*(pow((1+Rate/100),Time))
print("The Compound Interest is",Compound_interest)
