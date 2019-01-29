class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        now = last = 0
        for i in nums:
            last, now = now, max(i+last, now)
        return now
prices_1 = [2,1,1,2]
aa = Solution()
print(aa.rob(prices_1))
