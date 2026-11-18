# Last updated: 11/18/2026, 1:50:07 AM
1class ListNode:
2    def __init__(self, val, next=None):
3        self.val = val
4        self.next = next
5
6class MyLinkedList:
7
8    def __init__(self):
9        self.head = None
10        self.size = 0
11
12
13    def get(self, index: int) -> int:
14        if (index < 0) or (index >= self.size):
15            return -1
16        
17        cur = self.head
18        for _ in range(index):
19            cur = cur.next
20
21        return cur.val
22
23
24    def addAtHead(self, val: int) -> None:
25        return self.addAtIndex(0, val)
26
27
28    def addAtTail(self, val: int) -> None:
29        return self.addAtIndex(self.size, val)
30
31
32    def addAtIndex(self, index: int, val: int) -> None:
33        if (index < 0) or (index > self.size):
34            return 
35        
36        node = ListNode(val)
37    
38        if index == 0:
39            node.next = self.head
40            self.head = node
41
42        elif index == self.size:
43            cur = self.head
44            for _ in range(index-1):
45                cur = cur.next
46            cur.next = node
47        
48        else:
49            cur = self.head
50            for _ in range(index-1):
51                cur = cur.next
52            node.next = cur.next
53            cur.next = node 
54        
55        self.size += 1
56        
57        
58
59    def deleteAtIndex(self, index: int) -> None:
60        if (index < 0) or (index >= self.size):
61            return
62        
63        if index == 0:
64            self.head = self.head.next
65        
66        elif index == self.size - 1:
67            cur = self.head
68            for _ in range(index - 1):
69                cur = cur.next
70            cur.next = None
71        
72        else:
73            cur = self.head
74            for _ in range(index - 1):
75                cur = cur.next
76            cur.next = cur.next.next
77        
78        self.size -= 1
79
80
81# Your MyLinkedList object will be instantiated and called as such:
82# obj = MyLinkedList()
83# param_1 = obj.get(index)
84# obj.addAtHead(val)
85# obj.addAtTail(val)
86# obj.addAtIndex(index,val)
87# obj.deleteAtIndex(index)