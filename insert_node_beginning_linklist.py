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

    def node_at_begin(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode
    
    def node_at_end(self,newData):
        newNode = Node(newData)
        self.tail.next = newNode

    def node_at_after_existing_node(self,newData,existingData):
        runner = self.head
        newNode = Node(newData)
        existingNode = Node(existingData)
        while runner is not None:
            if runner.data is existingNode.data:
                newNode.next = runner.next
                runner.next = newNode
                break
            
            else:
                runner = runner.next

    def print_linklist(self):
        runner = self.head
        while runner is not None:
            print(runner.data)
            runner = runner.next
    
    


#######################################

li = [2, 3, 4, 5]
obj = Linklist(li)
obj.traverse_linklist_array()
obj.print_linklist()
print()
obj.node_at_begin(1)
obj.print_linklist()
print()
obj.node_at_end(6)
obj.print_linklist()
print()
obj.node_at_after_existing_node(7,3)
obj.print_linklist()


# let assume I want to add a value 1 at the beginning position of the linklist
