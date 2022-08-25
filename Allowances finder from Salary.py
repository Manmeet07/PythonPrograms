Basic=float(input("Enter Basic Salary:"))
DA=(Basic*135)/100
HRA=(Basic*30)/100
TA=(Basic*20)/100
GS=(DA+HRA+TA+Basic)
Tax=(Basic*10)/100
print("Dearness Allowance:",DA)
print("House Rent Allowance:",HRA)
print("Travel Allowance:",TA)
print("Gross Salary:",GS)
print("Tax;",Tax)
print("Gross Salary -Tax:",GS-Tax)
