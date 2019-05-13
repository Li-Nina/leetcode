# Definition for singly-linked list.
"""
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            node = l1
            while l1.next and l1.next.val <= l2.val:
                l1 = l1.next
            n = l1.next
            m = l2.next
            l1.next = l2
            after = l2
        else:
            node = l2
            while l2.next and l2.next.val < l1.val:
                l2 = l2.next
            n = l1.next
            m = l2.next
            l2.next = l1
            after = l1

        if n is None or m is None:
            if n:
                after.next = n
            elif m:
                after.next = m
            else:
                after.next = None
        else:
            after.next = self.mergeTwoLists(n, m)
        return node

    def mergeTwoLists_concise(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
