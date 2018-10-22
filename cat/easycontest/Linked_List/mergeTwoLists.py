# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head  = ListNode(0)
        node = head
        while l1 and l2:
            if l1.val > l2.val:
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node=node.next
        node.next = l1 if l1 else l2
        return head.next
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
while a:
    print(a.val)
    a = a.next