import pickle
D={}
f=open("Binop.Dat","ab")
N=int(input("How many records want to append:"))
for c in range(N):
    D["Roll"]=int(input("Enter Roll:"))
    D["Name"]=input("Enter Name:")
    pickle.dump(D,f)
f.close()
