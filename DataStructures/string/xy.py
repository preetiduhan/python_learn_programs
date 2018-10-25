'''
Created on Oct 14, 2018

@author: preeti
'''
def power(x,y):
    result=[0,0,0,0,0]
    if y==0 or y==1:
        return x
    elif(result[y-1]!=0):
        return result[y-1]
    else:
        result[y-1]=x*power(x,y-1)
    return result[y-1]

if __name__ == '__main__':
    x=power(2,5)
    print(x)