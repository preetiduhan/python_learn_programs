'''
Created on Oct 11, 2018

@author: preeti
'''

def fibo_rec(n):
    if n==1 or n==2:
        return 1
    else:
        return fibo_rec(n-1)+fibo_rec(n-2)

def fibo_iterative(n):
    a=1
    b=1
    while(n>2):
        c=a+b
        a=b
        b=c
        n=n-1
    return c


if __name__ == '__main__':
    x=fibo_rec(6)
    y=fibo_iterative(6)
    print(x)
    print(y)