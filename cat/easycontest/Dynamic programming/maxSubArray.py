class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)):
            if nums[i-1]>0:
                nums[i]=nums[i]+nums[i-1]
        return max(nums)
bb = [-1,2,4,-5,5,6,2]
aa = Solution()
print(aa.maxSubArray(bb))