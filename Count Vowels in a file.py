# e.g The books are stored in the library. The books were binded.- 18
f=open("DATA.TXT","r")
D=f.read()
v=0
L=['a','A','e','E','i','I','o','O','u','U']
for c in D:
    if c in L:
        v=v+1

f.close()
print("Total Counts of vowels is : ",v)
