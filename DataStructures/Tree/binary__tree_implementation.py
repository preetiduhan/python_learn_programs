'''
Created on Oct 21, 2018

@author: preeti
'''

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None

    def create_node(self,data):
        self.root=Node(data)
        return self.root


    def insert_node(self,root,data):
        if root==None:
            root=self.create_node(data)
        elif root.data > data:
            root.left=self.insert_node(root.left,data)
        else:
            root.right=self.insert_node(root.right,data)
        return root

    def sum_1(self,root):
        if(root == None):
            return
        elif (root.left == None) and (root.right == None):
            return root.data
        else:
            root.data = root.data + self.sum_1(root.left) + self.sum_1(root.right)
        return root

    def print_tree(self,root):
        if root==None:
            return
        self.print_tree(root.left)
        print(root.data,end='--')
        self.print_tree(root.right)

t=Tree()
root=t.create_node(4)
t.insert_node(root,5)
t.insert_node(root,7)
t.insert_node(root,2)
t.insert_node(root,10)
t.print_tree(root)
root=t.sum_1(root)
t.print_tree(root)