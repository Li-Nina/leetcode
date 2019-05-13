# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList_recursive(self, head: ListNode) -> ListNode:
        def reverse(node1, node2):
            n = node2.next
            node2.next = node1
            return reverse(node2, n) if n else node2

        if head:
            return reverse(None, head)

    def reverseList_iteration(self, head: ListNode) -> ListNode:
        pre = None
        while head:
            cur = head.next
            head.next = pre
            pre = head
            head = cur
        return pre
