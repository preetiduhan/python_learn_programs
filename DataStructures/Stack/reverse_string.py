from stack_implementation import Stack

def reverse(str):
    str2=[]
    s=Stack()
    for i in str:
        s.push(i)
    while(str != []):
        t=s.pop()
        str2.append(t)
    return str2

if __name__=='__main__':
    str="preeti"
    str=reverse(str)
    print(str)
