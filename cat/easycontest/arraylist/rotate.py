class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k:
            temp = nums[len(nums) - 1]
            for i in range(len(nums) - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = temp
            k = k - 1
        return nums


A = [1, 2, 3, 4, 5, 6, 7]
a = Solution().rotate(A, 3)
print(a)
