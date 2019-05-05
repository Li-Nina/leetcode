# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> 'ListNode':
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(head.next.next)
            p.next = head
            return p
        else:
            return head
