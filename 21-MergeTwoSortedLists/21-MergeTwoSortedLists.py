# Last updated: 4/19/2026, 11:24:06 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if (not list1) or (not list2):
            return list1 or list2
    
        if list1.val < list2.val:
            cur, oth = list1, list2
        else:
            cur, oth = list2, list1

        head = cur

        while cur:

            nex = cur.next

            if nex:
                if oth:
                    if oth.val < nex.val:
                        cur.next = oth
                        oth = nex

            else:
                if oth:
                    cur.next = oth
                    oth = nex

            cur = cur.next

        return head
