class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
a = "A man, a plan, a canal: Panama"
print(Solution().reverseString(a))
