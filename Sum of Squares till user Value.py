def Xsum_Squares(N):
   if (N==1):
      return (1)
   else:
      return (N*N)+(Xsum_Squares(N-1))

Num=int(input("Enter Number upto which u want sum of squares :"))
R=Xsum_Squares(Num)
print("Sum of squares :",R)
