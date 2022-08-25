def BinSearch(Arr,L,R,Num):
    if (R>=L):
        mid=(L+(R-L)//2)
        if A[mid]==Num:
            return mid
        elif A[mid]>Num:
            return BinSearch(Arr,L,mid-1,Num)
        else:
            return BinSearch(Arr,mid+1,R,Num)
    else:
        return (-1)

A=[1,2,3,4,5,6,7,8,9,10]
N=int(input("Enter Number To Search:"))
Result=BinSearch(A,0,len(A)-1,N)

if (Result!=-1):
    print("Found at ",Result)
else:
    print("Not Found ")
