def xfibo(n):
    if(n<=1):
        return(n)
    else:
        return (xfibo(n-1)+ xfibo(n-2))

N=int(input("Enter Fibonacci Terms:"))
for i in range(N):
    print(xfibo(i),end=" ")
   
