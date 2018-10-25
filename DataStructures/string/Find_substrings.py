'''
Created on Oct 14, 2018

@author: preeti
'''
def find_substrings(str):
    n=len(str)
    for l in range(1,len(str)+1):
        for j in range(n-l+1):
            end_index=l+j
            for k in range(j,end_index):
                print(str[k],end='')
            print(' ')

def find_left_string_sub(str):
    mid=int(len(str)/2)
    n=len(str)
    substrings=[[]]
    for l in range(1,mid+1):
        for j in range(mid-l+1):
            substring=[]
            for k in range(j,j+l):
                substring.append(str[k])
            substring=''.join(substring)
            substrings.append(substring)
    print(substrings)

if __name__ == '__main__':
    str='abcd'
    #find_substrings(str)
    find_left_string_sub(str)