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
    
    def delete_node(self,deleteData):

        #deleting 1st node
        if deleteData==self.head.data:
            self.head = self.head.next
            return
        
        #deleting any node after 1st node
        temp = None
        runner=self.head
        while runner is not None:
            if runner.data is deleteData:
                temp.next = runner.next
                return
            else:
                temp =  runner
                runner = runner.next
        return

    def print_linklist(self):
        runner = self.head
        while runner is not None:
            print(runner.data)
            runner = runner.next

#######################################
li = [1,2, 3, 4, 5]
obj = Linklist(li)
obj.traverse_linklist_array()
#obj.print_linklist()
#print()
obj.delete_node(4)
obj.print_linklist()

