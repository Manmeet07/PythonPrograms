f=open("DATA.TXT","r")
d=f.read().split()
count=0
for c in d:
    if(c=='The' or c=='the'):
        count=count+1

f.close()
print("Total counts for The and the are: ",count)
