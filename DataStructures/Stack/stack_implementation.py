class Stack:
    def __init__(self):
        self.items=[]

    def  is_empty(self):
        if (self.items == []):
            return True
        else:
            return False

    def push(self,item):
        self.items.insert(0,item)

    def pop(self):
        if(not self.is_empty()):
            item=self.items.pop()
            return item
        else:
            print("Stack is empty")

if __name__=='__main__':
    s=Stack()
    s.push('preeti')
    p=s.pop()
    s.push('duhan')
    print("popped item is %s "%p)
    d=s.pop()
    print("popped item is %s"%d)
