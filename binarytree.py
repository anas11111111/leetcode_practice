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

    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res += self.preorderTraversal(root.left)
            res += self.preorderTraversal(root.right)
        return res

    def postorderTraversal(self, root):
        res = []
        if root:
            res = self.preorderTraversal(root.left)
            res += self.preorderTraversal(root.right)
            res.append(root.data)
        return res

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res += self.inorderTraversal(root.right)
        return res

    def findInTree(self, val):
        if self.data > val:
            if self.left is None:
                return str(val) + " not found "
            return self.left.findInTree(val)
        elif self.data < val:
            if self.right is None:
                return str(val) + " not found "
            return self.right.findInTree(val)
        else:
            return str(self.data) + ' is found'


obj = Node(2)
obj.insert(5)
obj.insert(4)
obj.insert(3)
obj.insert(1)
obj.insert(20)
obj.insert(10)
obj.printTree()
print(obj.preorderTraversal(obj))
print(obj.postorderTraversal(obj))
print(obj.inorderTraversal(obj))
print(obj.findInTree(10))
print(obj.findInTree(16))
