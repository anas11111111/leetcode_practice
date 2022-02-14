class ListNode():
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class LinkList:
    def __init__(self) -> None:
        self.dummy = ListNode(-1)

    def insert(self, data):
        newNode = ListNode(data)
       
        current = self.dummy
        while(current.next):
            current = current.next
        current.next = newNode
       

    def println(self):
        runner = self.dummy.next
        while runner:
            print(runner.val)
            runner = runner.next

    def addTwoNumbers(self, l1, l2):
        runner1 = l1.next
        runner2 = l2.next
        carry = 0
        temp = LinkList()
        while runner1 or runner2:
            add = 0
            if runner1:
                add+=runner1.val
                runner1 = runner1.next
            if runner2:
                add+= runner2.val
                runner2 = runner2.next
            add +=carry
         
            if add >= 10:
                sum = add % 10
                temp.insert(sum)
                carry = 1
            else:
                sum = add
                temp.insert(sum)
                carry = 0
           
        if carry==1:
          temp.insert(carry)
        temp.println()

obj = LinkList()
obj.insert(2)
obj.insert(4)
obj.insert(3)

# obj.println()

obj1 = LinkList()
obj1.insert(5)
obj1.insert(6)
obj1.insert(4)
# obj1.println()

res = LinkList()
res.addTwoNumbers(obj.dummy, obj1.dummy)


#leetcode--version
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
        # dummy = p =ListNode(-1)
        # runner1 = l1
        # runner2 = l2
        # carry = 0
        # while runner1 or runner2:
        #     add = 0
        #     if runner1:
        #         add+=runner1.val
        #         runner1 = runner1.next
        #     if runner2:
        #         add+= runner2.val
        #         runner2 = runner2.next
        #     add +=carry
        #     if add >= 10:
        #         sum = add % 10
        #         p.next = ListNode(sum)
        #         carry = 1
        #     else:
        #         sum = add
        #         p.next = ListNode(sum)
        #         carry = 0
        #     p = p.next
        # if carry==1:
        #     p.next = ListNode(carry)
        
        # return dummy.next

