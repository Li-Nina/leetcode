# class Solution:
#     def isPalindrome(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         new_list = []
#         while not head or not head.next:
#             return True
#         slow, fast = head
#         while fast and fast.next:
#             new_list.insert(0,slow.val)
#             slow = slow.next
#             fast = fast.next.next
#         if fast:
#             slow = slow.next
#         for val in new_list:
#             if slow.val!= val:
#                 return False
#             slow = slow.next
#         return True
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while not head or not head.next:
            return True
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        slow = self.reverseList(slow)
        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True

    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre