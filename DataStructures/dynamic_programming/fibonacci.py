'''
Created on Oct 14, 2018

@author: preeti
'''
import  array
def fibo(n):
    fibo=[]
    for i in range(n):
        fibo.append(0)
    #print(fibo)
    fibo[0]=1
    fibo[1]=1
    for i in range(2,n):
        fibo[i]=fibo[i-1]+fibo[i-2]

    return fibo[n-1]

if __name__ == '__main__':
    n=10
    result=fibo(n)
    print(result)