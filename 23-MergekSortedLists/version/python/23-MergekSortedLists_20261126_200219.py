# Last updated: 11/26/2026, 8:02:19 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        if not lists:
            return None

        def mergeLists(list1, list2):

            if not (list1 and list2):
                return list1 or list2

            if list1.val < list2.val:
                list1.next = mergeLists(list1.next, list2)
                return list1
            else:
                list2.next = mergeLists(list1, list2.next)
                return list2

        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None
                temp.append(mergeLists(list1, list2))
            lists = temp

        return lists[0]