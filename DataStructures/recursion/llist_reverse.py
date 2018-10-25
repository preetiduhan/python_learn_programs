'''
Created on Oct 10, 2018

@author: preeti
'''

def bubble_sort(a,n):
    for i in range(0,n):
        if(i+1<n and a[i]>a[i+1]):
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp
    bubble_sort(a,n-1)

a=[12,4,5]
n=len(a)
print(n)
bubble_sort(a,n)
print(a)



