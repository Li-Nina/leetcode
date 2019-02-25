import re


def isBadVersion(check):
    pass


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

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        queue = []
        if root:
            queue.append(root)
        while queue:
            sub = []
            for i in queue:
                if i.left:
                    sub.append(i.left)
                if i.right:
                    sub.append(i.right)
            result.append([i.val for i in queue])
            queue = sub
        return result

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = (len(nums) - 1) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[0:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])
        return node

    res_dict = {}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            n_1 = self.res_dict.get(n - 1) if self.res_dict.get(n - 1) else self.climbStairs(n - 1)
            n_2 = self.res_dict.get(n - 2) if self.res_dict.get(n - 2) else self.climbStairs(n - 2)
            self.res_dict[n - 1] = n_1
            self.res_dict[n - 2] = n_2
            return n_1 + n_2

    def maxProfit(self, prices: 'List[int]') -> 'int':
        max_profit = 0
        if prices:
            min_price = prices[0]
            for i in prices:
                if min_price > i:
                    min_price = i
                elif i - min_price > max_profit:
                    max_profit = i - min_price
        return max_profit

    def maxSubArray(self, nums: 'List[int]') -> 'int':
        """
        Analysis of this problem:
        Apparently, this is a optimization problem, which can be usually solved by DP. So when it comes to DP, the first thing for us to figure out is the format of the sub problem(or the state of each sub problem). The format of the sub problem can be helpful when we are trying to come up with the recursive relation.
        At first, I think the sub problem should look like: maxSubArray(int A[], int i, int j), which means the maxSubArray for A[i: j]. In this way, our goal is to figure out what maxSubArray(A, 0, A.length - 1) is. However, if we define the format of the sub problem in this way, it's hard to find the connection from the sub problem to the original problem(at least for me). In other words, I can't find a way to divided the original problem into the sub problems and use the solutions of the sub problems to somehow create the solution of the original one.
        So I change the format of the sub problem into something like: maxSubArray(int A[], int i), which means the maxSubArray for A[0:i ] which must has A[i] as the end element. Note that now the sub problem's format is less flexible and less powerful than the previous one because there's a limitation that A[i] should be contained in that sequence and we have to keep track of each solution of the sub problem to update the global optimal value. However, now the connect between the sub problem & the original one becomes clearer:
        maxSubArray(A, i) = maxSubArray(A, i - 1) > 0 ? maxSubArray(A, i - 1) + A[i] : A[i] ;
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i] if nums[i - 1] > 0 else nums[i]
        return max(nums)

    the_nums = None
    rob_sub_dict = {}

    def rob(self, nums: 'List[int]') -> 'int':
        self.the_nums = nums
        self.rob_sub_dict = {}
        return self.rob_sub(len(self.the_nums) - 1)

    def rob_sub(self, end_index: int) -> int:
        if end_index < 0:
            self.rob_sub_dict[end_index] = 0
            return 0
        n1 = self.rob_sub_dict[end_index - 1] if self.rob_sub_dict.get(end_index - 1) is not None else self.rob_sub(
            end_index - 1)
        n2 = self.rob_sub_dict[end_index - 2] + self.the_nums[end_index] if self.rob_sub_dict.get(
            end_index - 2) is not None else self.rob_sub(end_index - 2) + self.the_nums[end_index]
        self.rob_sub_dict[end_index] = max(n1, n2)
        return self.rob_sub_dict[end_index]

    # The isBadVersion API is already defined for you.
    # @param version, an integer
    # @return a bool
    # def isBadVersion(version):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left_good = 1
        right_bad = n
        while left_good < right_bad:
            check = left_good + (right_bad - left_good) // 2
            if isBadVersion(check):
                right_bad = check
            else:
                left_good = check + 1
        return right_bad


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


# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(3)
# a.next = b
# b.next = c
# while a:
#     print(a.val)
#     a = a.next
# x = Solution().hehe()
# print(x)

if __name__ == '__main__':
    print(5 // 3)
