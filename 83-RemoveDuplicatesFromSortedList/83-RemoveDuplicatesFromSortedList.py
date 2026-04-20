# Last updated: 4/19/2026, 11:23:47 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        cur = head

        while cur.next:
    
            if cur.val == cur.next.val:
                cur.next = cur.next.next
                continue

            cur = cur.next

        return head

        