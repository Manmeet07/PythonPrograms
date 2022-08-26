f=open("DATA.TXT","w")
f.write("The books are stored in the library. The books were binded.")
f.close()

f=open("DATA.TXT","r")
d=f.read().split()
count=0
for c in d:
    print("\n",c)
    count=count+1

f.close()
print("\n Total words are: ",count)
