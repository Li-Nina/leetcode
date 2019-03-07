class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
               if nums[left]+nums[right] == -nums[i]:
                   result = []
                   result.append(nums[i])
                   result.append(nums[left])
                   result.append(nums[right])
                   if result not in res:
                       res.append(result)
                   left+=1
               elif nums[left]+nums[right]< -nums[i]:
                   left+=1
               elif nums[left]+nums[right]>-nums[i]:
                   right-=1
        return res
nums = [-1, 0, 1, 2, -1, -4]
aa = Solution()
print(aa.threeSum(nums))