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


x = Solution().strStr("helloll", "")
print(x)
