# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        head = rst = ListNode(-1)
        plus = 0
        while l1 and l2:
            v = l1.val + l2.val + plus
            val, plus = (v, 0) if v < 10 else (v - 10, v // 10)
            rst.next = ListNode(val)
            rst = rst.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            plus, rst = self.add_last(l1, plus, rst)
        elif l2:
            plus, rst = self.add_last(l2, plus, rst)
        if plus:
            rst.next = ListNode(plus)
        return head.next

    def add_last(self, node, plus, rst):
        while node:
            v = node.val + plus
            val, plus = (v, 0) if v < 10 else (v - 10, v // 10)
            rst.next = ListNode(val)  # 在方法内直接修改引用参数的内容是生效的。
            rst = rst.next  # 在方法内修改参数的索引引用，在方法外该参数是不生效的! 所以必须返回该参数，方法外接收。
            node = node.next
        return plus, rst


if __name__ == '__main__':
    a = ListNode(9)
    a.next = ListNode(9)
    b = ListNode(1)
    x = Solution().addTwoNumbers(a, b)
    while x:
        print(x.val)
        x = x.next
