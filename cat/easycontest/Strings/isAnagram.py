import collections


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        alpha = collections.defaultdict(int)
        alphb = collections.defaultdict(int)

        for i in s:
            alpha[i] += 1
        for j in t:
            alphb[j] += 1
        return True if alpha == alphb else False


s1 = "rat"
t1 = "tar"
print(Solution().isAnagram(s1, t1))
