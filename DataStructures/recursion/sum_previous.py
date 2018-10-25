'''
Created on Oct 9, 2018

@author: preeti
'''
def sum_previous(a,n):
    if(n<=1):
        return
    sum_previous(a,n-1)
    a[n-1] += a[n-2]

a=[1,2,3,4,8,10]
a=sum_previous(a, 1)
print(a)