class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=[]
        if n ==1 or n==2:
            return n
        elif n>=3:
            a.append(1)
            a.append(2)
            for i in range(2,n):
                a.append(a[i-1]+a[i-2])
            return a[n-1]
aa = Solution()
print(aa.climbStairs(4))

