import itertools

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n - 1):
            s = " ".join(str(len(list(group))) + digit for digit, group in itertools.groupby(s))
        return s


print(Solution().countAndSay(2))
x = (i for i in range(5))
print(list(x))
