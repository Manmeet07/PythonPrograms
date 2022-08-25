def QInsert(Arr):
    Num=int(input("Enter Number to be Inserted:"))
    Arr.append(Num)
    print("No. Addded ")

def QDelete(Arr):
    if (Arr==[]):
        print("Queue is Empty ")
    else:
        print("Element Deleted: ",Arr.pop(0))

def QDisplay(Arr):
    for c in Arr:
        print(c,"\t", end=" ")

Q=[]
ch='y'
while (ch=='y'):
    print("--------- Queue Menu System --------")
    print("1. Insert ")
    print("2. Delete")
    print("3. Display ")
    print("4. Exit ")
    c=int(input("Enter Your Choice 1/2/3/4 :"))
    if (c==1):
        QInsert(Q)
    elif (c==2):
        QDelete(Q)
    elif (c==3):
        QDisplay(Q)
    else:
        break
    ch=input("\n Do you want to continue y/n:")
