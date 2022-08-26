f=open("DATA.TXT","w")
f.write("Cool Cool India\nThey Live in Delhi")
f.write("\nCold is better than hot\nCooler gives us cold wind")
f.close()

f=open("DATA.TXT","r")
r=f.readline()
while(r):
    if(r[0]=='C'):
        print(r)
    r=f.readline()

f.close()
