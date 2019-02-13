import sys
n=int(input("Enter the no of lines : "))
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(0,(2*i-1)):
        if(k==0 or k==(2*i-2)):
           print("*",end="")
        else:
           print(" ",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(0,(2*i-1)):
        if(k==0 or k==(2*i-2)):
           print("*",end="")
        else:
           print(" ",end="")
    print()


