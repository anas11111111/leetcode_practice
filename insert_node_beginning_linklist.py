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
                print(temp.data)
                self.head = n
            else:
                print(n.data)
                temp.next = n
                temp = temp.next

        self.tail = temp

    def node_at_begin(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode
        print(self.head,newNode.next.data)
        print()

    def print_linklist_after_insertion(self):
        runner = self.head
        while runner is not None:
            print(runner.data)
            runner = runner.next  


li = [2, 3, 4, 5]
obj = Linklist(li)
obj.traverse_linklist_array()
print()
obj.node_at_begin(1)
obj.print_linklist_after_insertion()


# let assume I want to add a value 1 at the beginning position of the linklist
