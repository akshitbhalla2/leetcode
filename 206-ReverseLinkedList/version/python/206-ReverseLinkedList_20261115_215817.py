# Last updated: 11/15/2026, 9:58:17 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:

        if not head:
            return

        prv = None
        cur = head
        nxt = cur.next

        while nxt != None:
            cur.next = prv
            prv = cur
            cur = nxt
            nxt = cur.next

        cur.next = prv
        return cur
