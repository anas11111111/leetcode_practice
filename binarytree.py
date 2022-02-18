from pickle import NONE


class Node:
    def __init__(self, data=0, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data:
            if self.data > data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            elif self.data < data:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
    
obj = Node(2)
obj.insert(5)
obj.insert(4)
obj.insert(3)
obj.insert(1)
obj.insert(20)
obj.insert(10)
obj.printTree()
