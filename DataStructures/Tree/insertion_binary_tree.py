'''
Created on Oct 21, 2018

@author: preeti
'''
import queue
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree(Node):
    def __init__(self):
        self.root=None

    def insert_tree(self,root,data):
        l=queue.Queue()
        if root==None:
            root=Node(data)
            l.put(root.data)
            break
        if root.left==None:
            root.left=Node(data)
            break
        else:
            l.put(root.left.data)
        if root.right==None:
            root.right=Node(data)
            break
        else:
            l.put(root.right.data)








