class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree(Node):
    def __init__(self):
        self.root = None

    def addNode(self,data):
        return Node(data)

    def insert(self,root,data):
        if(root == None):
            root = self.addNode(data)
        else:
            if(data <= root.data):
               root.left = self.insert(root.left,data)
            else:
                root.right = self.insert(root.right,data)
        return root

    def PreOrder(self,root):
        if root == None:
            return
        else:
            print(root.data)
            self.PreOrder(root.left)
            self.PreOrder(root.right)

a = BinaryTree()
root = a.addNode(2)
#root = None
a.insert(root,4)
a.insert(root,34)
a.insert(root,45)
a.insert(root,46)
a.insert(root,41)
a.insert(root,48)
a.PreOrder(root)
