'''
Created on Oct 15, 2018

@author: preeti
'''
#from _overlapped import NULL

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Tree:
    '''
    classdocs
    '''
    def __init__(self):
        self.root = None

    def __insert(self, data):
        self.root = self.insert_node(self.root, data)

    def insert_node(self,node,data):
        if(node == None) :
            node=Node(data)
        elif node.data > data:
            node.left=self.insert_node(node.left,data)
        else:
            node.right=self.insert_node(node.right,data)
        return node

    def __sum(self):
        self.root=self.sum(self.root)

    def sum(self,root):
        temp=self.root
        if(root == None):
            return
        elif (temp.left == None) and (temp.right == None):
            return temp.data
        else:
            temp.data = temp.data + self.sum_1(temp.left) + self.sum_1(temp.right)

    def __print_nodes(self):
        self.print_nodes(self.root)

    def print_nodes(self,node):
        if node ==None:
            return
        self.print_nodes(node.left)
        print(node.data)
        self.print_nodes(node.right)

t=Tree()
t.__insert(5)
t.print_tree()
t.__insert(6)
t.print_tree()
t.__insert(10)
t.print_tree()
t.__insert(1)
t.print_tree()
t.sum()
t.print_tree()
