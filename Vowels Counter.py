String=str(input("Enter a String:"))
Vowels=0
for i in String:
    if(i=='A'or i=='E'or i=='I'or i=='O'
       or i=='U'or i=='a'or i=='e'
       or i=='i'or i=='o'or i=='u'):
        Vowels=Vowels+1
print("Number of vowels are",Vowels)
