import pickle
D={}
f=open("Binop.Dat","wb")
N=int(input("How many records want to input:"))
for c in range(N):
    D["Roll"]=int(input("Enter Roll:"))
    D["Name"]=input("Enter Name:")
    pickle.dump(D,f)
f.close()
