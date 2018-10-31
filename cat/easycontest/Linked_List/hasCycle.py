# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = q = head
        while p and p.next:
            p = p.next.next
            q = q.next
            if p == q:
                return True
        return False
