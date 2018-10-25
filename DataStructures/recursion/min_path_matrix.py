'''
Created on Oct 13, 2018

@author: preeti
'''
import numpy as np

def min_path(m,s,d):
    if(s==d or s==d-1):
        return m[s][d]
    min_cost=m[s][d]
    i=s+1
    for i in range(d):
        cost=min_path(s,i)+min_path(i,d)
        if(cost<min_cost):
            min_cost=cost

m=[]
print(m)
min_path(m,0,5)