#!/bin/python3
import sys
import random
def factorial(n):
    if(n==0):
        return 1
    else:
        return (n*factorial(n-1))
def ncr(n,r):
    k=int(factorial(n)/(factorial(r)*factorial(n-r)))
    return k
if __name__ == "__main__":
    n, m, x = input().strip().split(' ')
    n, m, x = [int(n), int(m), int(x)]
    a = list(map(int, input().strip().split(' ')))
    p=len(a)
    count=0
    for i in range(1,p+1):
        n=ncr(p,i)
        for j in range(1,n+1):
            l=random.sample(a,i)
            k=len(l)
            for k1 in range(0,k):
                l[k1]=l[k1]%m
            c=1
            for k1 in range(0,k):
                c*=l[k1]
            if(c%m==x):
                count+=1
print(count)
                
            
            
        
    
