import re


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # if needle == '':
        #     return 0
        # elif re.search(needle,haystack):
        #     return re.search(needle,haystack).span()[0]
        # else:
        #     return -1
        m = re.search(needle, haystack)
        return m.span()[0] if m else -1


aa = "accaa"
bb = ""
print(Solution().strStr(aa, bb))
