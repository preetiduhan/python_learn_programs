from threading import *

class baseclass(Thread):
    def __init__(self,a):
        Thread.__init__(self)
        print(a)
    def run(self):
        print("thread chhalu ho gaya")

t=baseclass(5)
t.start()





