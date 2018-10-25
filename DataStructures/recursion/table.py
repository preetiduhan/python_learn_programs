'''
Created on Oct 10, 2018

@author: preeti
'''
def table(n,i):
    if(i>10):
        return;
    else:
        result=n*i
        print(result ,end=' ')
        table(n,i+1)

if __name__ == '__main__':
    table(5,1)