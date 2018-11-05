import re


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        result = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
        return result

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {val: i for (i, val) in enumerate(nums)}
        for i, val in enumerate(nums):
            j = dic.get(target - val)
            if j is not None and j != i:
                return [i, j]

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for index, val in enumerate(nums):
            j = dic.get(target - val)
            if j is not None and j != index:
                return [j, index]
            dic[val] = index

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        if x[0] == '-':
            return int('-' + x[:0:-1]) if -2 ** 31 <= int('-' + x[:0:-1]) <= 2 ** 31 - 1 else 0
        else:
            return int(x[::-1]) if -2 ** 31 <= int(x[::-1]) <= 2 ** 31 - 1 else 0

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        result = len(s)
        for i, v in enumerate(s):
            dic[v] = (1 if dic.get(v) is None else dic.get(v)[0] + 1, i)
        for k, v in dic.items():
            result = v[1] if v[0] == 1 and v[1] < result else result
        return result if result != len(s) else -1

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return ''.join(sorted(s)) == ''.join(sorted(t))

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = [i for i in s.lower() if i.isalnum()]
        return m == m[::-1]

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        int_str = []
        for c in str.lstrip():
            if c.isdigit():
                int_str.append(c)
            elif not int_str and (c == '+' or c == '-'):
                int_str.append(c)
            else:
                break
        if int_str and not (len(int_str) == 1 and not int_str[0].isdigit()):
            result = int(''.join(int_str))
            if result > 2147483647:
                return 2147483647
            elif result < -2147483648:
                return -2147483648
            else:
                return result
        else:
            return 0

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = re.compile(needle).search(haystack)
        return m.span()[0] if m else -1

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        pre_head = None
        node = head
        while node:
            tmp = node.next
            node.next, pre_head = pre_head, node
            node = tmp
        return pre_head

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        pre_head = None
        node = head
        while node:
            tmp = node.next
            node.next, pre_head = pre_head, node
            node = tmp
        return pre_head

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        node = head
        while l1 and l2:
            if l1.val > l2.val:
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node = node.next
        node.next = l1 if l1 else l2
        return head.next

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        begin = head
        while head and head.next:
            if head.next == begin:
                return True
            n = head.next
            head.next = begin
            head = n
        return False

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return left + 1 if left > right else right + 1

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []

        def recurse(node):
            if node:
                recurse(node.left)
                res.append(node.val)
                recurse(node.right)

        recurse(root)
        if res:
            pre = res[0]
            for r in res[1:]:
                if r <= pre:
                    return False
                pre = r
        return True

    def isValidBST2(self, root, lo=-float('inf'), hi=float('inf')):
        if not root:
            return True
        elif not lo < root.val < hi:  # validate the root's value
            return False

        return self.isValidBST2(root.left, lo, root.val) and self.isValidBST2(root.right, root.val, hi)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.check(root.left, root.right)
        else:
            return True

    def check(self, left, right):
        if not left or not right:
            return not left and not right
        elif left.val != right.val:
            return False
        else:
            return self.check(left.left, right.right) and self.check(left.right, right.left)

    def isSymmetric2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        q = [root.left, root.right]
        while q:
            n1 = q.pop()
            n2 = q.pop()
            if not n1 and not n2:
                pass
            elif not n1 or not n2:
                return False
            elif n1.val != n2.val:
                return False
            else:
                q.append(n1.left)
                q.append(n2.right)
                q.append(n1.right)
                q.append(n2.left)
        return True


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
while a:
    print(a.val)
    a = a.next
# x = Solution().hehe()
# print(x)
