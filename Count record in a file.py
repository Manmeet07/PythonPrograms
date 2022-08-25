import pickle
D={}
count=0
f=open("Binop.Dat","rb")
try:
    while True:
        D=pickle.load(f)
        print(D)
        count=count+1
except EOFError:
    print("Total Number of Records are:",count)
    pass
f.close()
