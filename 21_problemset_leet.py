from cProfile import run
from logging.config import valid_ident
import re


class ListNode:
    def __init__(self ,val = 0,next=None)->None:
        self.val = val
        self.next = next

class LinkList:
    def __init__(self) -> None:
        self.dummy = ListNode(-1)
    
    def insert(self,data):
        newNode = ListNode(data)
        current =self.dummy
        while current.next:
            current = current.next
        
        current.next = newNode
    
    def println(self):
        runner = self.dummy.next
        while runner:
            print(runner.val)
            runner = runner.next
    def mergeTwoLists(self,list1,list2):
        runner1 =list1.next
        runner2 =list2.next
        temp = LinkList()

        while runner1 or runner2:
            if runner1 and runner2:
                if runner1.val<= runner2.val:
                    temp.insert(runner1.val)
                    runner1 = runner1.next
                else:
                    temp.insert(runner2.val)
                    runner2 = runner2.next
            elif runner1:
                temp.insert(runner1.val)
                runner1 =runner1.next
            else:
                temp.insert(runner2.val)
                runner2 = runner2.next
        temp.println()

obj = LinkList()
obj.insert(1)
obj.insert(2)
obj.insert(4)

# obj.println()

obj1 = LinkList()
obj1.insert(1)
obj1.insert(3)
obj1.insert(4)
# obj1.println()

res = LinkList()
res.mergeTwoLists(obj.dummy,obj1.dummy)


