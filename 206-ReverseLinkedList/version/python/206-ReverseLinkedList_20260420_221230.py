# Last updated: 4/20/2026, 10:12:30 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        pre = None
9        cur = head
10        while cur:
11            nex = cur.next
12            cur.next = pre
13            pre = cur
14            cur = nex
15    
16        return pre