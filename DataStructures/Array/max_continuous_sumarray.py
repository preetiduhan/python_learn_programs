'''
Created on Oct 24, 2018

@author: preeti
'''

n=input("enter n:\n")
arr=input()
l=list(map(int,arr.split(' ')))
max=0
new_max=0
for i in range(len(l)):
    new_max=0
    for j in range(i,len(l)):
        new_max=new_max+l[j]
        #print("i=%d and new_max=%d"%(i,new_max))
        if(new_max>max):
            max=new_max
print("max value is %d"% max)



