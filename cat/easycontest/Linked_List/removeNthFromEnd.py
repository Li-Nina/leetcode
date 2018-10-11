# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        next = head
        for i in range(n):
            next = next.next
        to_delete_pre = head
        while next is not None and next.next is not None:
            to_delete_pre = to_delete_pre.next
            next = next.next

        if next is None and to_delete_pre == head:
            head = head.next
        else:
            to_delete_pre.next = to_delete_pre.next.next
        return head


