from threading import *

class MyThread:
    def __init__(self,a):
        self.a=a
    def run(self):
        print("chall jaa thread")

t=MyThread(2)
thread1=Thread(target=t.run)
thread1.start()
