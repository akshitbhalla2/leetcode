# Last updated: 11/15/2026, 9:58:17 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: ListNode | None) -> ListNode | None:
8
9        if not head:
10            return 
11        
12        prv = None
13        cur = head
14        nxt = cur.next
15
16        while nxt != None:
17            cur.next = prv
18            prv = cur
19            cur = nxt
20            nxt = cur.next 
21
22        cur.next = prv     
23        return cur