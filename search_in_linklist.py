class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Linklist:
    def __init__(self, li) -> None:
        self.head = Node(None)
        self.tail = Node(None)
        self.li = li
    
    def traverse_linklist_array(self):
        li = self.li
        temp = None
        for i in li:
            n = Node(i)
            if temp is None:
                temp = n
                self.head = n
            else:
                temp.next = n
                temp = temp.next
        self.tail = temp
    
    def search_node(self,val):
        runner = self.head
        while runner is not None:
            if runner.data==val:
                return True
            else:
                runner = runner.next
        return False

    def print_linklist(self):
        runner = self.head
        while runner is not None:
            print(runner.data)
            runner = runner.next

li = [1,2, 3, 4, 5]
obj = Linklist(li)
obj.traverse_linklist_array()
#obj.print_linklist()
if obj.search_node(51):
    print('Node is found')
else:
    print('Node is not found')