# Last updated: 4/19/2026, 11:22:30 PM
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:

        if (index < 0) or (index >= self.size):
            return -1

        cur = self.head
        for _ in range(index):
            cur = cur.next

        return cur.val

    def addAtHead(self, val: int) -> None:    
        node = ListNode(val, self.head)
        self.head = node
        
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = ListNode(val, None)

        if not self.head:
            self.head = node
        else:
            cur = self.head
            for _ in range(self.size-1):
                cur = cur.next
            
            cur.next = node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        
        if (index < 0) or (index > self.size):
            return 

        if index == 0:
            return self.addAtHead(val)

        if index == self.size:
            return self.addAtTail(val)

        cur = self.head
        for _ in range(index-1):
            cur = cur.next

        node = ListNode(val, cur.next)
        cur.next = node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:

        if (index < 0) or (index >= self.size):
            return 

        if index == 0:
            self.head = self.head.next
        
        else:
            cur = self.head
            for _ in range(index-1):
                cur = cur.next
            
            cur.next = cur.next.next

        self.size -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)