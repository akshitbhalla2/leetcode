# Last updated: 11/15/2026, 11:45:45 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
8
9        if not list1:
10            return list2
11        
12        if not list2:
13            return list1
14
15        if list1.val < list2.val:
16            list1.next = self.mergeTwoLists(list1.next, list2)
17            return list1
18        else:
19            list2.next = self.mergeTwoLists(list1, list2.next)
20            return list2