def SPush(Arr):
    Num=int(input("Enter Number to be push :"))
    Arr.append(Num)
    print("No. Addded ")

def SPop(Arr):
    if (Arr==[]):
        print("Stack is Empty ")
    else:
        print("Element Poped: ",Arr.pop())

def SDisplay(Arr):
    D=Arr.copy()
    D.reverse()
    for c in D:
        print(c)

S=[]
ch='y'
while (ch=='y'):
    print("--------- Stack Menu System --------")
    print("1. Push ")
    print("2. Pop")
    print("3. Travsal ")
    print("4. Exit ")
    c=int(input("Enter Your Choice 1/2/3/4 :"))
    if (c==1):
        SPush(S)
    elif (c==2):
        SPop(S)
    elif (c==3):
        SDisplay(S)
    else:
        break
    ch=input("Do you want to continue y/n ")
