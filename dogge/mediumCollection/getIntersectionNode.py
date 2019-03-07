# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        two pointer, curA and curB
        curA走完listA后指向listB，curB走完listB后指向listA。
        如果有交点，curA和curB必在交点处相遇。如果没有交点，curA和curB必同时走向末尾，指向null
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA = headA
        curB = headB
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        return curA
