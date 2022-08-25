import pickle
D={}
flag=0
f=open("Binop.Dat","rb")
R=int(input("Enter Roll No. to be search:"))

try:
    while True:
        D=pickle.load(f)
        if (D["Roll"]==R):
            print("Found")
            print(D)
            flag=1
            break
except EOFError:
    pass
    
if(flag==0):
    print("Not Found")
f.close()
