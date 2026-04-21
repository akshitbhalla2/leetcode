# Last updated: 4/20/2026, 10:04:22 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        # pre = None
9        # cur = head
10
11        # nex = cur.next
12        # cur.next = pre
13        # pre = cur
14        # cur = nex
15        # nex = cur.next
16        # cur.next = pre
17        # pre = cur
18        # cur = nex
19        # nex = cur.next
20        # cur.next = pre
21        
22        pre = None
23        cur = head
24        while cur != None:
25            nex = cur.next
26            cur.next = pre
27            pre = cur
28            cur = nex
29    
30        return pre