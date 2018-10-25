'''
Created on Oct 9, 2018

@author: preeti
'''

def fact(n):
    if n==0 | n==1:
        return 1
    else:
        return n+fact(n-1)


if __name__ == '__main__':
    n=fact(3)
    print(n)