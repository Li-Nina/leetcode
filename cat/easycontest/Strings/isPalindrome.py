class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = [i for i in s.lower() if i.isalnum()]
        return m==m[::-1]





s1 = "rat"
t1 = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(t1))
