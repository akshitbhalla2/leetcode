# Last updated: 11/26/2026, 8:02:19 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
8
9        if not lists:
10            return None
11
12        def mergeLists(list1, list2):
13
14            if not (list1 and list2):
15                return list1 or list2
16
17            if list1.val < list2.val:
18                list1.next = mergeLists(list1.next, list2)
19                return list1
20            else:
21                list2.next = mergeLists(list1, list2.next)
22                return list2
23
24        while len(lists) > 1:
25            temp = []
26            for i in range(0, len(lists), 2):
27                list1 = lists[i]
28                list2 = lists[i+1] if (i+1) < len(lists) else None 
29                temp.append(mergeLists(list1, list2))
30            lists = temp
31
32        return lists[0]
33
34        