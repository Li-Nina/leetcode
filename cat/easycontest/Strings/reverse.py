class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)

        if x[0] == '-':
            return int('-' + x[:0:-1]) if -2**31<=int('-' + x[:0:-1])<=2**31-1 else 0
        else:
            return int(x[::-1]) if -2**31<=int(x)<=2**31-1 else 0


b = -1
print(Solution().reverse(b))

